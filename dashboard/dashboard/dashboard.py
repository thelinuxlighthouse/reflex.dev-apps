import reflex as rx
import psutil
import distro


class MonitorState(rx.State):
    cpu: float = 0.0
    memory: float = 0.0
    disk: float = 0.0
    os_flav: str = ""
    distro_name = distro.name()
    distro_version = distro.version()
    distro_id = distro.id()

    @rx.event
    def update_metrics(self):
        self.cpu = psutil.cpu_percent(interval=0)
        self.memory = psutil.virtual_memory().percent
        self.disk = psutil.disk_usage("/").percent
        self.os_flav = psutil.os.uname().nodename

    @rx.var
    def cpu_int(self) -> int:
        return int(self.cpu)

    @rx.var
    def memory_int(self) -> int:
        return int(self.memory)

    @rx.var
    def disk_int(self) -> int:
        return int(self.disk)


def stat_card(label, progress_value, float_value, color):
    return rx.card(
        rx.vstack(
            rx.text(label, size="3", color_scheme=color),
            rx.progress(value=progress_value, max=100, color_scheme=color, size="3"),
            rx.text(f"{float_value:.1f}%", size="5", color_scheme=color, weight="bold"),
        ),
        padding="2",
        shadow="lg",
        # Responsive width: full width on mobile, less on larger screens
        width=rx.breakpoints(initial="100%", md="80%", lg="250px"),
        align="center",
    )


def index() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="bottom-right"),
        rx.heading(
            "System Monitoring Dashboard",
            color_scheme="green",
            size=rx.breakpoints(initial="7", xs="7", sm="7", md="8", lg="9"),
            class_name="pt-4",
        ),
        rx.text(
            f"Hostname: {MonitorState.os_flav}",
            size="6",
            font_weight="bold",
            color_scheme="sky",
        ),
        rx.text(
            f"Linux Distribution: {MonitorState.distro_name}, Version: {MonitorState.distro_version}, ID: {MonitorState.distro_id}",
            size=rx.breakpoints(initial="2", xs="2", sm="2", md="5", lg="5"),
            font_weight="bold",
            color_scheme="amber",
        ),
        # Responsive stack: vertical on mobile, horizontal on desktop
        rx.hstack(
            stat_card("CPU Usage", MonitorState.cpu_int, MonitorState.cpu, "red"),
            stat_card(
                "Memory Usage", MonitorState.memory_int, MonitorState.memory, "blue"
            ),
            stat_card("Disk Usage", MonitorState.disk_int, MonitorState.disk, "orange"),
            spacing="4",
            wrap="wrap",
        ),
        rx.moment(
            interval=2000,
            on_change=MonitorState.update_metrics,
            display="none",
        ),
        spacing="6",
        padding="4",
        align="center",
    )


app = rx.App()
app.add_page(index, route="/")
