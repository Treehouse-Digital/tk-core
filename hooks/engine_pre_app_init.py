"""Definition of the EnginePreAppInit hook base class."""

from sgtk import get_hook_baseclass
from sgtk.platform.engine import Engine


class EnginePreAppInit(get_hook_baseclass()):
    """Hook executed in every `.Engine.__init__` just before `.Engine.pre_app_init`.

    Called using old-style Tank core hook execution i.e. via
    `.PipelineConfiguration.execute_call_hook_internal`.

    At this point, all apps and frameworks have been loaded, and the engine is fully
    operational. The default implementation does nothing.
    """

    def execute(self, engine: Engine) -> None:
        """Actions to run for given engine."""
