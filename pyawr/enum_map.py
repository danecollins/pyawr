
# This file defines functions which can reverse map AWRDE api enumerations to strings
#
# generated automatically by pyawr/const_map.py and should not be manually edited.
#
# This file will raise an exception if an illegal value is passed in.


def mwAlignToolFlags(value):
    items = {
             2: "mwATF_Bottom",
             32: "mwATF_HorzCenter",
             8: "mwATF_Left",
             16: "mwATF_Right",
             128: "mwATF_SpaceH",
             64: "mwATF_SpaceV",
             1: "mwATF_Top",
             4: "mwATF_VertCenter",
            }
    return items[value]


def mwApplicationAttributeType(value):
    items = {
             17: "mwAAT_AppAttributeCount",
             8: "mwAAT_AppName",
             9: "mwAAT_AppNameDetailed",
             15: "mwAAT_AppProgId",
             7: "mwAAT_AppStreamVersion",
             5: "mwAAT_AppVersion",
             6: "mwAAT_AppVersionShort",
             4: "mwAAT_BuildNumber",
             14: "mwAAT_BuildRevision",
             3: "mwAAT_ClientDirectory",
             2: "mwAAT_EnvIniFilePath",
             10: "mwAAT_FoundryProcName",
             1: "mwAAT_IniFilePath",
             16: "mwAAT_LicenseInfo",
             13: "mwAAT_ProcessID",
             12: "mwAAT_RegressionCaptureMode",
             11: "mwAAT_TestMode",
            }
    return items[value]


def mwApplicationDirectoryType(value):
    items = {
             21: "mwADT_Analog",
             1: "mwADT_AppData",
             3: "mwADT_AppDataCommon",
             6: "mwADT_AppDataLibraryCache",
             5: "mwADT_AppDataLogs",
             2: "mwADT_AppDataUser",
             0: "mwADT_AppDir",
             11: "mwADT_Cells",
             25: "mwADT_CurrentProject",
             15: "mwADT_Data",
             27: "mwADT_DesignKits",
             26: "mwADT_Documents",
             9: "mwADT_EmModels",
             18: "mwADT_EmModelsUser",
             7: "mwADT_Examples",
             16: "mwADT_HSpice",
             8: "mwADT_Libraries",
             20: "mwADT_LibraryCache",
             19: "mwADT_Logs",
             28: "mwADT_Measurements",
             10: "mwADT_Models",
             22: "mwADT_Projects",
             23: "mwADT_Scripts",
             24: "mwADT_ScriptsUser",
             13: "mwADT_Signals",
             12: "mwADT_Symbols",
             4: "mwADT_TempFile",
             17: "mwADT_TestResults",
             14: "mwADT_Textures",
            }
    return items[value]


def mwApplicationFileType(value):
    items = {
             1: "mwAFT_CommonIni",
             3: "mwAFT_Customizations",
             4: "mwAFT_DataCache",
             7: "mwAFT_EMSightCache",
             6: "mwAFT_Executable",
             5: "mwAFT_FlexLmLicense",
             10: "mwAFT_GlobalScript",
             8: "mwAFT_MWOfficeExe",
             9: "mwAFT_Project",
             0: "mwAFT_Temporary",
             2: "mwAFT_UserIni",
            }
    return items[value]


def mwArcAttributes(value):
    items = {
             1: "mwAA_CenterX",
             2: "mwAA_CenterY",
             0: "mwAA_LayerIndex",
             6: "mwAA_Length",
             3: "mwAA_Radius",
             4: "mwAA_StartAngle",
             5: "mwAA_StopAngle",
            }
    return items[value]


def mwAreaAddType(value):
    items = {
             0: "mwAAT_ContainedObjects",
             1: "mwAAT_OverlappedObjects",
            }
    return items[value]


def mwArrayCellAttributes(value):
    items = {
             2: "mwACA_ArrayCellCols",
             3: "mwACA_ArrayCellDx",
             4: "mwACA_ArrayCellDy",
             1: "mwACA_ArrayCellRows",
             0: "mwACA_IsArrayCell",
            }
    return items[value]


def mwBooleanCornerStyles(value):
    items = {
             0: "mwBCS_CornerRounded",
             1: "mwBCS_CornerSharp",
            }
    return items[value]


def mwBooleanEngineVersions(value):
    items = {
             2: "mwBEV_BooleanBoost",
             3: "mwBEV_BooleanClipper",
             0: "mwBEV_BooleanLatest",
             1: "mwBEV_BooleanPolyBool",
            }
    return items[value]


def mwBoundaryModelType(value):
    items = {
             2: "mwBMT_ApproximateOpen",
             5: "mwBMT_Dielectric",
             3: "mwBMT_InfiniteWaveguide",
             0: "mwBMT_PerfectConductor",
             4: "mwBMT_ReadConductor",
             1: "mwBMT_SpecifiedMaterial",
            }
    return items[value]


def mwCellExportFormat(value):
    items = {
             1: "mwCEF_DXF",
             0: "mwCEF_GDSII",
            }
    return items[value]


def mwCellLibraryType(value):
    items = {
             1: "mwCLT_DXF",
             0: "mwCLT_GDSII",
             2: "mwCLT_OA",
            }
    return items[value]


def mwCellStretcherAttributes(value):
    items = {
             6: "mwCSA_ArrowHeight",
             7: "mwCSA_IsBound",
             5: "mwCSA_LowerLimit",
             2: "mwCSA_Multipler",
             3: "mwCSA_Offset",
             1: "mwCSA_ParameterName",
             8: "mwCSA_Region",
             0: "mwCSA_StretchType",
             4: "mwCSA_UpperLimit",
            }
    return items[value]


def mwColor(value):
    items = {
             16775408: "mwCLR_AliceBlue",
             14150650: "mwCLR_AntiqueWhite",
             16776960: "mwCLR_Cyan",
             13959039: "mwCLR_Aquamarine",
             16777200: "mwCLR_Azure",
             14480885: "mwCLR_Beige",
             12903679: "mwCLR_Bisque",
             0: "mwCLR_Black",
             13495295: "mwCLR_BlanchedAlmond",
             16711680: "mwCLR_Blue",
             14822282: "mwCLR_BlueViolet",
             2763429: "mwCLR_Brown",
             8894686: "mwCLR_BurlyWood",
             10526303: "mwCLR_CadetBlue",
             65407: "mwCLR_Chartreuse",
             1993170: "mwCLR_Chocolate",
             5275647: "mwCLR_Coral",
             15570276: "mwCLR_CornflowerBlue",
             14481663: "mwCLR_Cornsilk",
             3937500: "mwCLR_Crimson",
             9109504: "mwCLR_DarkBlue",
             9145088: "mwCLR_DarkCyan",
             755384: "mwCLR_DarkGoldenrod",
             11119017: "mwCLR_DarkGray",
             25600: "mwCLR_DarkGreen",
             7059389: "mwCLR_DarkKhaki",
             9109643: "mwCLR_DarkMagenta",
             3107669: "mwCLR_DarkOliveGreen",
             36095: "mwCLR_DarkOrange",
             13382297: "mwCLR_DarkOrchid",
             139: "mwCLR_DarkRed",
             8034025: "mwCLR_DarkSalmon",
             9157775: "mwCLR_DarkSeaGreen",
             9125192: "mwCLR_DarkSlateBlue",
             5197615: "mwCLR_DarkSlateGray",
             13749760: "mwCLR_DarkTurquoise",
             13828244: "mwCLR_DarkViolet",
             9639167: "mwCLR_DeepPink",
             16760576: "mwCLR_DeepSkyBlue",
             6908265: "mwCLR_DimGray",
             16748574: "mwCLR_DodgerBlue",
             2237106: "mwCLR_Firebrick",
             15792895: "mwCLR_FloralWhite",
             2263842: "mwCLR_ForestGreen",
             16711935: "mwCLR_Magenta",
             14474460: "mwCLR_Gainsboro",
             16775416: "mwCLR_GhostWhite",
             55295: "mwCLR_Gold",
             2139610: "mwCLR_Goldenrod",
             8421504: "mwCLR_Gray",
             32768: "mwCLR_Green",
             3145645: "mwCLR_GreenYellow",
             15794160: "mwCLR_Honeydew",
             11823615: "mwCLR_HotPink",
             6053069: "mwCLR_IndianRed",
             8519755: "mwCLR_Indigo",
             15794175: "mwCLR_Ivory",
             9234160: "mwCLR_Khaki",
             16443110: "mwCLR_Lavender",
             16118015: "mwCLR_LavenderBlush",
             64636: "mwCLR_LawnGreen",
             13499135: "mwCLR_LemonChiffon",
             15128749: "mwCLR_LightBlue",
             8421616: "mwCLR_LightCoral",
             16777184: "mwCLR_LightCyan",
             13826810: "mwCLR_LightGoldenrodYellow",
             13882323: "mwCLR_LightGray",
             9498256: "mwCLR_LightGreen",
             12695295: "mwCLR_LightPink",
             8036607: "mwCLR_LightSalmon",
             11186720: "mwCLR_LightSeaGreen",
             16436871: "mwCLR_LightSkyBlue",
             10061943: "mwCLR_LightSlateGray",
             14599344: "mwCLR_LightSteelBlue",
             14745599: "mwCLR_LightYellow",
             65280: "mwCLR_Lime",
             3329330: "mwCLR_LimeGreen",
             15134970: "mwCLR_Linen",
             128: "mwCLR_Maroon",
             11193702: "mwCLR_MediumAquamarine",
             13434880: "mwCLR_MediumBlue",
             13850042: "mwCLR_MediumOrchid",
             14381203: "mwCLR_MediumPurple",
             7451452: "mwCLR_MediumSeaGreen",
             15624315: "mwCLR_MediumSlateBlue",
             10156544: "mwCLR_MediumSpringGreen",
             13422920: "mwCLR_MediumTurquoise",
             8721863: "mwCLR_MediumVioletRed",
             7346457: "mwCLR_MidnightBlue",
             16449525: "mwCLR_MintCream",
             14804223: "mwCLR_MistyRose",
             11920639: "mwCLR_Moccasin",
             11394815: "mwCLR_NavajoWhite",
             8388608: "mwCLR_Navy",
             15136253: "mwCLR_OldLace",
             32896: "mwCLR_Olive",
             2330219: "mwCLR_OliveDrab",
             42495: "mwCLR_Orange",
             17919: "mwCLR_OrangeRed",
             14053594: "mwCLR_Orchid",
             11200750: "mwCLR_PaleGoldenrod",
             10025880: "mwCLR_PaleGreen",
             15658671: "mwCLR_PaleTurquoise",
             9662683: "mwCLR_PaleVioletRed",
             14020607: "mwCLR_PapayaWhip",
             12180223: "mwCLR_PeachPuff",
             4163021: "mwCLR_Peru",
             13353215: "mwCLR_Pink",
             14524637: "mwCLR_Plum",
             15130800: "mwCLR_PowderBlue",
             8388736: "mwCLR_Purple",
             255: "mwCLR_Red",
             9408444: "mwCLR_RosyBrown",
             14772545: "mwCLR_RoyalBlue",
             1262987: "mwCLR_SaddleBrown",
             7504122: "mwCLR_Salmon",
             6333684: "mwCLR_SandyBrown",
             5737262: "mwCLR_SeaGreen",
             15660543: "mwCLR_SeaShell",
             2970272: "mwCLR_Sienna",
             12632256: "mwCLR_Silver",
             15453831: "mwCLR_SkyBlue",
             13458026: "mwCLR_SlateBlue",
             9470064: "mwCLR_SlateGray",
             16448255: "mwCLR_Snow",
             8388352: "mwCLR_SpringGreen",
             11829830: "mwCLR_SteelBlue",
             9221330: "mwCLR_Tan",
             8421376: "mwCLR_Teal",
             14204888: "mwCLR_Thistle",
             4678655: "mwCLR_Tomato",
             13688896: "mwCLR_Turquoise",
             15631086: "mwCLR_Violet",
             11788021: "mwCLR_Wheat",
             16777215: "mwCLR_White",
             16119285: "mwCLR_WhiteSmoke",
             65535: "mwCLR_Yellow",
             3329434: "mwCLR_YellowGreen",
            }
    return items[value]


def mwComponentTestResultType(value):
    items = {
             1: "mwDMT_TestRunPerformanceData",
             0: "mwDMT_TestRunResultData",
            }
    return items[value]


def mwDashStyle(value):
    items = {
             1: "mwLineSolid",
             2: "mwLineThick",
             4: "mwLineThickThin",
             3: "mwLineThin",
            }
    return items[value]


def mwDataFileType(value):
    items = {
             6: "mwDFT_DSCR",
             5: "mwDFT_GMDIF",
             7: "mwDFT_GMDIFD",
             2: "mwDFT_IV",
             4: "mwDFT_MDIF",
             1: "mwDFT_RAW",
             0: "mwDFT_SNP",
             3: "mwDFT_TXT",
            }
    return items[value]


def mwDataSetFlags(value):
    items = {
             262144: "mwDSF_ClockStringReset",
             0: "mwDSF_Default",
             32768: "mwDSF_DisableAutoDelete",
             524288: "mwDSF_DistSimResult",
             4096: "mwDSF_DocCleanOnOpen",
             32: "mwDSF_ForOptimization",
             65536: "mwDSF_ForTuning",
             131072: "mwDSF_ForYield",
             1048576: "mwDSF_InMemoryDataSet",
             64: "mwDSF_IncludesG3DModel",
             16: "mwDSF_IncludesGeometry",
             1024: "mwDSF_IncompleteDataSet",
             1: "mwDSF_IsPartialDataSet",
             2048: "mwDSF_KeepReadStreamOpen",
             128: "mwDSF_KeepSweepValOrder",
             512: "mwDSF_KeepWriteStreamOpen",
             2: "mwDSF_MeshOnly",
             256: "mwDSF_NoAutoLoadInProject",
             4: "mwDSF_NotFinalIter",
             8192: "mwDSF_Pinned",
             8: "mwDSF_PortOnly",
             16384: "mwDSF_Updating",
            }
    return items[value]


def mwDefRouteConnModelTypes(value):
    items = {
             1: "mwDRCM_CenterlineAndAdjacent",
             0: "mwDRCM_CenterlineModel",
            }
    return items[value]


def mwDefaultFaceAlignType(value):
    items = {
             0: "mwDFA_Center",
             1: "mwDFA_Variable",
            }
    return items[value]


def mwDesignRuleErrorFileFormat(value):
    items = {
             0: "mwDREF_AWR",
             2: "mwDREF_Assura",
             1: "mwDREF_Calibre",
            }
    return items[value]


def mwDesignRuleState(value):
    items = {
             2: "mwDRS_CheckedError",
             0: "mwDRS_Error",
             1: "mwDRS_FalseError",
            }
    return items[value]


def mwDesignRuleType(value):
    items = {
             8: "mwDRT_Angle",
             16: "mwDRT_Edge",
             4: "mwDRT_Extension",
             6: "mwDRT_ExtensionInv",
             2: "mwDRT_Jog",
             13: "mwDRT_MaxSideLength",
             12: "mwDRT_MaxVertices",
             15: "mwDRT_MultiPolygon",
             10: "mwDRT_MustHaveHole",
             9: "mwDRT_NoHole",
             1: "mwDRT_Notch",
             18: "mwDRT_Notch_In",
             19: "mwDRT_Notch_Out",
             14: "mwDRT_ObjectError",
             11: "mwDRT_OnGrid",
             5: "mwDRT_Overlap",
             17: "mwDRT_Polygon",
             7: "mwDRT_PolygonArea",
             3: "mwDRT_Seperation",
             20: "mwDRT_Unknown",
             0: "mwDRT_Width",
            }
    return items[value]


def mwDesignViewType(value):
    items = {
             0: "mwDVT_DesignView2D",
             1: "mwDVT_DesignView3D",
            }
    return items[value]


def mwDiagramLockLevel(value):
    items = {
             1: "mwDLL_LockedForEdit",
             2: "mwDLL_LockedForViewing",
             0: "mwDLL_Unlocked",
            }
    return items[value]


def mwDimensionArrowLocation(value):
    items = {
             0: "mwDAL_Inside",
             1: "mwDAL_Outside",
            }
    return items[value]


def mwDimensionTextLocation(value):
    items = {
             0: "mwDTL_CenterPar",
             1: "mwDTL_CenterPer",
             3: "mwDTL_LeftPar",
             2: "mwDTL_RightPar",
            }
    return items[value]


def mwDisplayModeType(value):
    items = {
             2: "mwDMT_BuddySelected",
             4: "mwDMT_BuddyUnselected",
             1: "mwDMT_Highlighted",
             16: "mwDMT_ObjectCondemned",
             8: "mwDMT_ObjectMarked",
            }
    return items[value]


def mwDockBorder(value):
    items = {
             2: "mwDB_Bottom",
             3: "mwDB_Left",
             4: "mwDB_Right",
             1: "mwDB_Top",
            }
    return items[value]


def mwDockState(value):
    items = {
             1: "mwDS_Docked",
             2: "mwDS_Floating",
             3: "mwDS_Normal",
            }
    return items[value]


def mwDrawingArcDirection(value):
    items = {
             1: "mwDAD_Clockwise",
             0: "mwDAD_CounterClockwise",
            }
    return items[value]


def mwDrawingShapeType(value):
    items = {
             2: "mwDST_Arc",
             8: "mwDST_Arrow",
             6: "mwDST_Ellipse",
             1: "mwDST_Line",
             3: "mwDST_Polygon",
             4: "mwDST_Polyline",
             7: "mwDST_Rectangle",
             5: "mwDST_Text",
             0: "mwDST_Unknown",
            }
    return items[value]


def mwDrawingSubObjectType(value):
    items = {
             1: "mwDSO_CutoutCircle",
             2: "mwDSO_CutoutEllipse",
             0: "mwDSO_CutoutPolygon",
            }
    return items[value]


def mwDrawingTextAttributes(value):
    items = {
             4: "mwDTA_Bold",
             3: "mwDTA_Font",
             1: "mwDTA_Height",
             5: "mwDTA_Italic",
             2: "mwDTA_Text",
            }
    return items[value]


def mwEECmdShow(value):
    items = {
             0: "mwEECS_Hide",
             1: "mwEECS_Show",
            }
    return items[value]


def mwEMGroupType(value):
    items = {
             4: "mwEMG_Coupled",
             3: "mwEMG_Mutual",
             0: "mwEMG_None",
             1: "mwEMG_NoneOld",
             2: "mwEMG_Series",
            }
    return items[value]


def mwEMInitType(value):
    items = {
             2: "mwEMI_Default",
             1: "mwEMI_LPF",
             0: "mwEMI_Stackup",
            }
    return items[value]


def mwEMInputDataXMLType(value):
    items = {
             0: "mwEIX_EMSocketDataFile",
             1: "mwEIX_EMSocketSimplifiedDataFile",
            }
    return items[value]


def mwEMMeshDensity(value):
    items = {
             0: "mwEMMD_High",
             2: "mwEMMD_Medium",
             1: "mwEMMD_Normal",
             3: "mwEMME_Low",
            }
    return items[value]


def mwEMPortFlags(value):
    items = {
             0: "mwEMF_Default",
             1: "mwEMF_EdgeToGround",
             16: "mwEMF_EndOfTypes",
             4: "mwEMF_ExtendAsMetal",
             8: "mwEMF_ExtendUpDown",
             2: "mwEMF_ExtendUpward",
            }
    return items[value]


def mwEMPortType(value):
    items = {
             3: "mwEMP_Bottom",
             6: "mwEMP_CenterX",
             7: "mwEMP_CenterY",
             13: "mwEMP_Extract",
             11: "mwEMP_FullLine",
             9: "mwEMP_GapX",
             10: "mwEMP_GapY",
             12: "mwEMP_HalfLine",
             2: "mwEMP_Left",
             1: "mwEMP_None",
             4: "mwEMP_Right",
             5: "mwEMP_Top",
             8: "mwEMP_Via",
            }
    return items[value]


def mwEMShapePortType(value):
    items = {
             1: "mwSPT_EdgePort",
             4: "mwSPT_ExtractPort",
             2: "mwSPT_InternalPort",
             3: "mwSPT_ViaPort",
            }
    return items[value]


def mwEMSolverToleranceLevel(value):
    items = {
             2: "mwEMSL_High",
             0: "mwEMSL_Low",
             1: "mwEMSL_Medium",
             3: "mwEMSL_VeryHigh",
            }
    return items[value]


def mwEMSolverType(value):
    items = {
             0: "mwEMST_DefaultDirect",
             1: "mwEMST_FullDirect",
             6: "mwEMST_IterativeCustom",
             3: "mwEMST_IterativeLarge",
             4: "mwEMST_IterativeMedium",
             5: "mwEMST_IterativeSmall",
             2: "mwEMST_SymetricDirect",
            }
    return items[value]


def mwElementType(value):
    items = {
             0: "mwET_Circuit",
             1: "mwET_System",
            }
    return items[value]


def mwEllipseAttributes(value):
    items = {
             1: "mwEA_Area",
             4: "mwEA_Eccentricity",
             3: "mwEA_Height",
             0: "mwEA_LayerIndex",
             2: "mwEA_Width",
            }
    return items[value]


def mwEmExtractAtrributes(value):
    items = {
             1: "mwEEA_GroupName",
             0: "mwEEA_IsEMExtract",
            }
    return items[value]


def mwEmSimulator(value):
    items = {
             5: "mwEMS_AwrAce",
             4: "mwEMS_AwrAnalyst",
             0: "mwEMS_AwrAxiem",
             1: "mwEMS_AwrAxiem32",
             2: "mwEMS_AwrAxiem64",
             3: "mwEMS_AwrEmSight",
             9: "mwEMS_CST",
             11: "mwEMS_CSTAsync",
             10: "mwEMS_HFSSAsync",
             8: "mwEMS_OeaNetan",
             12: "mwEMS_SonnetAsync",
             6: "mwEMS_SonnetEm",
             7: "mwEMS_ZelandIe3d",
            }
    return items[value]


def mwEmbeddedDocType(value):
    items = {
             4: "mwEDT_EMLayout",
             5: "mwEDT_EMLayout3D",
             7: "mwEDT_Graph",
             1: "mwEDT_Schematic",
             2: "mwEDT_SchematicLayout",
             3: "mwEDT_SchematicLayout3D",
             6: "mwEDT_SystemDiagram",
             0: "mwEDT_Unknown",
            }
    return items[value]


def mwEquationDataType(value):
    items = {
             1: "mwEDT_Complex",
             11: "mwEDT_ComplexVector",
             5: "mwEDT_DataModel",
             4: "mwEDT_ElementName",
             8: "mwEDT_Enumeration",
             10: "mwEDT_FileName",
             6: "mwEDT_InfoString",
             2: "mwEDT_Integer",
             7: "mwEDT_None",
             0: "mwEDT_Real",
             9: "mwEDT_RealVector",
             3: "mwEDT_String",
            }
    return items[value]


def mwEquationVariableType(value):
    items = {
             2: "mwEVT_DisplayValue",
             1: "mwEVT_ParameterDefinition",
             0: "mwEVT_VariableDefinition",
            }
    return items[value]


def mwErrorType(value):
    items = {
             2: "mwET_Error",
             3: "mwET_Fatal",
             0: "mwET_None",
             1: "mwET_Warning",
            }
    return items[value]


def mwExclusiveOrShapesType(value):
    items = {
             1: "mwEST_ExclusiveOrOnDestinationLayer",
             0: "mwEST_ExclusiveOrOnExistingLayers",
            }
    return items[value]


def mwExternalEditorType(value):
    items = {
             2: "mwEET_OrionEditor",
             1: "mwEET_SpaceClaimEditor",
            }
    return items[value]


def mwFaceAlignment(value):
    items = {
             5: "mwFA_Adapt",
             1: "mwFA_Center",
             0: "mwFA_Left",
             3: "mwFA_OffsetFix",
             4: "mwFA_OffsetVar",
             2: "mwFA_Right",
            }
    return items[value]


def mwFaceGroupType(value):
    items = {
             2: "mwFGT_MustConnectPinGroup",
             0: "mwFGT_StrongPinGroup",
             1: "mwFGT_WeakPinGroup",
            }
    return items[value]


def mwFaceInsetOptions(value):
    items = {
             8: "mwFIO_InsetAllOneDbUnit",
             6: "mwFIO_InsetAllOneHalfDbUnit",
             5: "mwFIO_InsetAllOneQtrDbUnit",
             7: "mwFIO_InsetAllThreeQtrDbUnit",
             4: "mwFIO_InsetNonOrthogOneDbUnit",
             2: "mwFIO_InsetNonOrthogOneHalfDbUnit",
             1: "mwFIO_InsetNonOrthogOneQtrDbUnit",
             3: "mwFIO_InsetNonOrthogThreeQtrDbUnit",
             0: "mwFIO_NoInset",
            }
    return items[value]


def mwFaceMultiLayerProperty(value):
    items = {
             4: "mwFLP_Bridge1",
             5: "mwFLP_Bridge2",
             6: "mwFLP_Bridge3",
             7: "mwFLP_Bridge4",
             0: "mwFLP_Default",
             1: "mwFLP_Flush",
             2: "mwFLP_Inside",
             3: "mwFLP_Outside",
            }
    return items[value]


def mwFaceShapeType(value):
    items = {
             1: "mwFST_AreaFaceType",
             0: "mwFST_SegmentFaceType",
            }
    return items[value]


def mwFeatureTypeFlags(value):
    items = {
             64: "mwFTF_AdvancedMWO",
             32: "mwFTF_AdvancedSystem",
             1: "mwFTF_CircuitSimulator",
             4: "mwFTF_EMSimulator",
             8: "mwFTF_Layout",
             128: "mwFTF_MMIC",
             2: "mwFTF_NonLinearSimulator",
             16: "mwFTF_SystemSimulator",
            }
    return items[value]


def mwFillStyle(value):
    items = {
             21: "mwFS_BackwardDiagonal",
             17: "mwFS_Brick",
             5: "mwFS_Checkered",
             16: "mwFS_CoarseGridPoint",
             24: "mwFS_Cross",
             25: "mwFS_DiagonalCross",
             18: "mwFS_DotCross",
             8: "mwFS_FineBackwardDiagonal",
             2: "mwFS_FineCross",
             3: "mwFS_FineDiagonalCross",
             9: "mwFS_FineForwardDiagonal",
             10: "mwFS_FineHorizontal",
             12: "mwFS_FineVertical",
             20: "mwFS_ForwardDiagonal",
             6: "mwFS_GridPoint",
             11: "mwFS_HeavyHorizontal",
             13: "mwFS_HeavyVertical",
             22: "mwFS_Horizontal",
             4: "mwFS_InverseCross",
             7: "mwFS_InverseFineCross",
             19: "mwFS_LaceRows",
             14: "mwFS_MediumHorizontal",
             15: "mwFS_MediumVertical",
             0: "mwFS_None",
             1: "mwFS_Solid",
             23: "mwFS_Vertical",
            }
    return items[value]


def mwGraphColorIndex(value):
    items = {
             0: "mwGCI_Black",
             3: "mwGCI_Blue",
             5: "mwGCI_Brown",
             6: "mwGCI_Cyan",
             8: "mwGCI_Gray",
             2: "mwGCI_Green",
             9: "mwGCI_LtGray",
             4: "mwGCI_Magenta",
             1: "mwGCI_Red",
             7: "mwGCI_Yellow",
            }
    return items[value]


def mwGraphLegendStyleIndex(value):
    items = {
             2: "mwGLE_BothNames",
             0: "mwGLE_DataName",
             1: "mwGLE_MeasurementName",
            }
    return items[value]


def mwGraphLineStyleIndex(value):
    items = {
             1: "mwGLS_DashedLine",
             3: "mwGLS_DotDashLine",
             2: "mwGLS_DottedLine",
             0: "mwGLS_SolidLine",
            }
    return items[value]


def mwGraphLineWeightIndex(value):
    items = {
             0: "mwGLW_1PixelWidth",
             1: "mwGLW_2PixelWidth",
             2: "mwGLW_3PixelWidth",
             3: "mwGLW_4PixelWidth",
             4: "mwGLW_5PixelWidth",
            }
    return items[value]


def mwGraphMarkerFormat(value):
    items = {
             2: "mwGMF_DbMagnitudeAngle",
             1: "mwGMF_MagnitudeAngle",
             0: "mwGMF_RealImaginary",
            }
    return items[value]


def mwGraphMarkerType(value):
    items = {
             2: "mwGMT_Admittance",
             1: "mwGMT_Impdedence",
             0: "mwGMT_ReflectionCoefficient",
             3: "mwGMT_Unknown",
            }
    return items[value]


def mwGraphType(value):
    items = {
             5: "mwGT_Antenna",
             8: "mwGT_Constellation",
             6: "mwGT_Histogram",
             1: "mwGT_Polar",
             3: "mwGT_Rectangular",
             2: "mwGT_SmithChart",
             4: "mwGT_Tabular",
             7: "mwGT_ThreeDim",
            }
    return items[value]


def mwGraphYieldDisplayStyle(value):
    items = {
             0: "mwGYD_AllTraces",
             2: "mwGYD_Failed",
             3: "mwGYD_Mean",
             1: "mwGYD_Passed",
            }
    return items[value]


def mwGraphYieldRangeStyle(value):
    items = {
             1: "mwGYR_Envelope",
             0: "mwGYR_MinAndMax",
             2: "mwGYR_RangeBox",
            }
    return items[value]


def mwHatchStyle(value):
    items = {
             5: "mwHS_BackwardDiagonal",
             6: "mwHS_Cross",
             7: "mwHS_DiagonalCross",
             4: "mwHS_ForwardDiagonal",
             2: "mwHS_Horizontal",
             0: "mwHS_None",
             1: "mwHS_Solid",
             3: "mwHS_Vertical",
            }
    return items[value]


def mwINetModelingLevel(value):
    items = {
             3: "mwNML_Distrubuted",
             4: "mwNML_EmExtraction",
             1: "mwNML_RCLumped",
             2: "mwNML_RLCLumped",
             0: "mwNML_ShortCircuits",
            }
    return items[value]


def mwImportProjectRenameItems(value):
    items = {
             0: "mwIPRI_All",
             1: "mwIPRI_Conflicted",
            }
    return items[value]


def mwImportProjectRenameStyle(value):
    items = {
             0: "mwIPI_AddPrefix",
             1: "mwIPI_AddSuffix",
            }
    return items[value]


def mwInstanceExportOptions(value):
    items = {
             3: "mwIEO_AppendLibNameToAll",
             2: "mwIEO_AppendLibNameToDuplicates",
             1: "mwIEO_AppendNumberToDuplicates",
             0: "mwIEO_NoChangesToCellNames",
            }
    return items[value]


def mwInterpolationCoords(value):
    items = {
             0: "mwIC_Cartesian",
             1: "mwIC_Polar",
            }
    return items[value]


def mwInterpolationMethod(value):
    items = {
             0: "mwIM_Linear",
             1: "mwIM_RationalFunction",
             2: "mwIM_SplineCurve",
            }
    return items[value]


def mwIntersectShapesType(value):
    items = {
             0: "mwIST_IntersectOnExistingLayers",
             1: "mwIST_IntersectToDestinationLayer",
            }
    return items[value]


def mwJobStatusType(value):
    items = {
             9: "mwJS_Canceled",
             7: "mwJS_Canceling",
             11: "mwJS_Crashed",
             8: "mwJS_Ended",
             12: "mwJS_Failed",
             10: "mwJS_Killed",
             2: "mwJS_Pending",
             14: "mwJS_Receiving",
             1: "mwJS_Rejected",
             4: "mwJS_Removed",
             5: "mwJS_Running",
             3: "mwJS_Scheduled",
             13: "mwJS_Sending",
             6: "mwJS_Suspended",
             0: "mwJS_Unknown",
            }
    return items[value]


def mwLVSHighlightLoc(value):
    items = {
             2: "mwLVSHL_HighlightInLayout",
             3: "mwLVSHL_HighlightInSchemAndLay",
             1: "mwLVSHL_HighlightInSchematic",
             0: "mwLVSHL_NoHighlighting",
            }
    return items[value]


def mwLayout3DPlacementAttributes(value):
    items = {
             0: "mwTDP_EmLayer",
             2: "mwTDP_XAngle",
             3: "mwTDP_YAngle",
             1: "mwTDP_ZOffset",
            }
    return items[value]


def mwLayoutArcAttributes(value):
    items = {
             0: "mwLAA_CenterX",
             1: "mwLAA_CenterY",
             2: "mwLAA_Radius",
             3: "mwLAA_StartAngle",
             4: "mwLAA_StopAngle",
            }
    return items[value]


def mwLayoutCellAttributes(value):
    items = {
             3: "mwLCA_Anchor",
             5: "mwLCA_CellName",
             6: "mwLCA_ElementName",
             4: "mwLCA_Frozen",
             2: "mwLCA_LayerMappingIndex",
             0: "mwLCA_LineTypeIndex",
             1: "mwLCA_UsesProcessLayers",
            }
    return items[value]


def mwLayoutCellExportOptions(value):
    items = {
             1: "mwLCE_ExportAsInstancesOption",
             0: "mwLCE_ExportFlattenedOption",
             2: "mwLCE_ExportSpecifiedAsInstances",
            }
    return items[value]


def mwLayoutCellShapeAttributes(value):
    items = {
             0: "mwLCS_CellName",
             1: "mwLCS_IsArtwork",
            }
    return items[value]


def mwLayoutCellStretcherAttributes(value):
    items = {
             7: "mwLCS_ArrowHeight",
             6: "mwLCS_Direction",
             5: "mwLCS_IsBound",
             4: "mwLCS_LowerLimit",
             1: "mwLCS_Multiplier",
             2: "mwLCS_Offset",
             0: "mwLCS_ParameterName",
             3: "mwLCS_UpperLimit",
            }
    return items[value]


def mwLayoutConnectionLineTypes(value):
    items = {
             1: "mwLCL_CenterPointLines",
             2: "mwLCL_MinimumSpanningLines",
             0: "mwLCL_StaightLines",
            }
    return items[value]


def mwLayoutDimensionLineAttributes(value):
    items = {
             2: "mwDLA_ArrowLength",
             0: "mwDLA_ArrowLocation",
             3: "mwDLA_GapLength",
             8: "mwDLA_Length",
             7: "mwDLA_LengthTolerance",
             4: "mwDLA_Precision",
             6: "mwDLA_ShowTolerance",
             5: "mwDLA_ShowUnits",
             1: "mwDLA_TextLocation",
            }
    return items[value]


def mwLayoutDragLayoutObjectAttributes(value):
    items = {
             1: "mwDLO_StretchToFix",
             0: "mwDLO_UseForAnchor",
            }
    return items[value]


def mwLayoutDrillHoleAttributes(value):
    items = {
             0: "mwDHA_DrillHoleIndex",
            }
    return items[value]


def mwLayoutEllipseAttributes(value):
    items = {
             0: "mwLEA_Area",
             3: "mwLEA_Eccentricity",
             2: "mwLEA_Height",
             1: "mwLEA_Width",
            }
    return items[value]


def mwLayoutExportFormat(value):
    items = {
             2: "mwLEF_DXF",
             4: "mwLEF_DrillFile",
             1: "mwLEF_GDSII_Flat",
             0: "mwLEF_GDSII_Hierarchical",
             3: "mwLEF_Gerber",
             5: "mwLEF_Pads",
            }
    return items[value]


def mwLayoutFaceAttributes(value):
    items = {
             3: "mwFAT_AngleOffset",
             0: "mwFAT_FaceJustification",
             1: "mwFAT_XOffset",
             2: "mwFAT_YOffset",
            }
    return items[value]


def mwLayoutFontAttributes(value):
    items = {
             1: "mwLFA_BoldStyle",
             3: "mwLFA_FontHeight",
             0: "mwLFA_FontName",
             2: "mwLFA_ItalicStyle",
            }
    return items[value]


def mwLayoutGroupAttributes(value):
    items = {
             0: "mwLGA_GroupChildCount",
            }
    return items[value]


def mwLayoutLayerAttributes(value):
    items = {
             0: "mwLLA_LayerName",
            }
    return items[value]


def mwLayoutMagnificationAttributes(value):
    items = {
             0: "mwLMA_Magnification",
            }
    return items[value]


def mwLayoutNetShapeAttributes(value):
    items = {
             1: "mwLNS_Associated",
             0: "mwLNS_NetworkId",
            }
    return items[value]


def mwLayoutObjectSelectFilters(value):
    items = {
             8192: "mwLSF_AreaPin",
             131072: "mwLSF_ArtworkCell",
             4096: "mwLSF_CellPort",
             262144: "mwLSF_EMPort",
             1: "mwLSF_Graphics",
             256: "mwLSF_LayCell",
             1048576: "mwLSF_LayModifier",
             16384: "mwLSF_LayPort",
             0: "mwLSF_None",
             512: "mwLSF_SubCell",
             4: "mwLSF_Text",
             64: "mwLSF_iNet",
            }
    return items[value]


def mwLayoutOrientationAttributes(value):
    items = {
             0: "mwLOA_FixedPosition",
             1: "mwLOA_FlipState",
             2: "mwLOA_RotationAngle",
            }
    return items[value]


def mwLayoutParamDataType(value):
    items = {
             4: "mwLPDT_IntVector",
             1: "mwLPDT_Integer",
             0: "mwLPDT_Real",
             3: "mwLPDT_RealVector",
             2: "mwLPDT_String",
            }
    return items[value]


def mwLayoutPathAttributes(value):
    items = {
             4: "mwLPA_BeginExt",
             5: "mwLPA_EndExt",
             6: "mwLPA_Length",
             2: "mwLPA_MiterType",
             3: "mwLPA_OffsetMiterAmount",
             1: "mwLPA_PathEndType",
             0: "mwLPA_PathWidth",
            }
    return items[value]


def mwLayoutPinAttributes(value):
    items = {
             1: "mwLPA_ConnectType",
             3: "mwLPA_GroupType",
             2: "mwLPA_PinGroup",
             0: "mwLPA_PortNumber",
            }
    return items[value]


def mwLayoutPolyAttributes(value):
    items = {
             0: "mwLP_Area",
            }
    return items[value]


def mwLayoutPolylineAttributes(value):
    items = {
             0: "mwLPLA_Length",
            }
    return items[value]


def mwLayoutRouteGravity(value):
    items = {
             0: "mwLRG_NoneGravity",
             2: "mwLRG_NormalGravity",
             3: "mwLRG_StrongGravity",
             1: "mwLRG_WeakGravity",
            }
    return items[value]


def mwLayoutRoutePathAttributes(value):
    items = {
             1: "mwLRP_Associated",
             0: "mwLRP_NetworkId",
            }
    return items[value]


def mwLayoutRulerAttributes(value):
    items = {
             1: "mwLRA_GapLength",
             9: "mwLRA_Length",
             6: "mwLRA_MinorTickHeight",
             5: "mwLRA_MinorTickSpacing",
             3: "mwLRA_Precision",
             0: "mwLRA_RulerSpacing",
             8: "mwLRA_ShowLabels",
             7: "mwLRA_ShowMinorTicks",
             4: "mwLRA_ShowUnits",
             2: "mwLRA_TickHeight",
            }
    return items[value]


def mwLayoutRulerTickLocation(value):
    items = {
             -1: "mwLRT_AboveRuler",
             1: "mwLRT_BelowRuler",
            }
    return items[value]


def mwLayoutSelectMode(value):
    items = {
             0: "mwLSM_AutoSelect",
             1: "mwLSM_ManualSelect",
            }
    return items[value]


def mwLayoutShapeAttributes(value):
    items = {
             3: "mwLSA_LayerIndex",
             2: "mwLSA_LayerMappingIndex",
             0: "mwLSA_LineTypeIndex",
             1: "mwLSA_UsesProcessLayers",
            }
    return items[value]


def mwLayoutSnapMode(value):
    items = {
             0: "mwLSM_Auto",
             1: "mwLSM_Manual",
             2: "mwLSM_Selected",
            }
    return items[value]


def mwLayoutSnapType(value):
    items = {
             0: "mwLST_AllObjects",
             1: "mwLST_SelectedOnly",
            }
    return items[value]


def mwLayoutSubcircuitAttributes(value):
    items = {
             0: "mwLSA_MasterDocName",
            }
    return items[value]


def mwLayoutTextAttributes(value):
    items = {
             2: "mwLTA_ArrowPointX",
             3: "mwLTA_ArrowPointY",
             1: "mwLTA_DrawTextArrow",
             0: "mwLTA_DrawTextAsPoly",
             4: "mwLTA_TextString",
            }
    return items[value]


def mwLayoutViewDetails(value):
    items = {
             0: "mwLVD_AllDetails",
             2: "mwLVD_LowDetails",
             1: "mwLVD_NormalDetails",
             3: "mwLVD_VeryLowDetails",
            }
    return items[value]


def mwLayoutWindowType(value):
    items = {
             0: "mwLWT_Layout2D",
             1: "mwLWT_Layout3D",
            }
    return items[value]


def mwLibraryElementType(value):
    items = {
             3: "mwLET_DataFile",
             1: "mwLET_Model",
             4: "mwLET_Subcircuit",
             0: "mwLET_Unknown",
             2: "mwLET_XML",
            }
    return items[value]


def mwLineMarkerTrackType(value):
    items = {
             2: "mwLMT_LeftYAxis",
             3: "mwLMT_RightYAxis",
             1: "mwLMT_XAxis",
            }
    return items[value]


def mwLineMarkerType(value):
    items = {
             1: "mwLM_HorizontalLineMarker",
             2: "mwLM_VerticalLineMarker",
            }
    return items[value]


def mwLineStyle(value):
    items = {
             1: "mwLS_Dash",
             3: "mwLS_DashDot",
             4: "mwLS_DashDotDot",
             2: "mwLS_Dot",
             0: "mwLS_Solid",
            }
    return items[value]


def mwLinearSolveType(value):
    items = {
             2: "mwLST_Full",
             0: "mwLST_Smart",
             1: "mwLST_Sparse",
            }
    return items[value]


def mwMarkerAutoSearchMode(value):
    items = {
             0: "mwMAM_Max",
             1: "mwMAM_Min",
             2: "mwMAM_Peak",
             3: "mwMAM_Valley",
             4: "mwMAM_Value",
             5: "mwMAM_XIndex",
            }
    return items[value]


def mwMarkerOffsetMode(value):
    items = {
             0: "mwMOM_X",
             1: "mwMOM_Y",
            }
    return items[value]


def mwMarkerSearchDirection(value):
    items = {
             1: "mwMSD_SearchLeft",
             0: "mwMSD_SearchRight",
            }
    return items[value]


def mwMarkerSearchMode(value):
    items = {
             0: "mwMST_Absolute",
             1: "mwMST_Delta",
            }
    return items[value]


def mwMarkerSearchVariable(value):
    items = {
             0: "mwMSV_X",
             1: "mwMSV_Y",
            }
    return items[value]


def mwMarkerSymbolType(value):
    items = {
             10: "mwMST_Circle",
             11: "mwMST_Cross",
             3: "mwMST_Diamond",
             4: "mwMST_HourGlass",
             8: "mwMST_LineDownDiagonal",
             5: "mwMST_LineHorizontal",
             7: "mwMST_LineUpDiagonal",
             6: "mwMST_LineVertical",
             0: "mwMST_None",
             12: "mwMST_Plus",
             2: "mwMST_Rectangle",
             9: "mwMST_TriangleDown",
             1: "mwMST_TriangleUp",
            }
    return items[value]


def mwMarkerType(value):
    items = {
             3: "mwMT_AutoSearch",
             2: "mwMT_DataSet",
             0: "mwMT_Normal",
             4: "mwMT_Offset",
             1: "mwMT_Parameter",
            }
    return items[value]


def mwMeasDataType(value):
    items = {
             2: "mwMDT_AdmittanceData",
             7: "mwMDT_CurveTraceData",
             13: "mwMDT_DiscreteTimeData",
             4: "mwMDT_GainCircleData",
             10: "mwMDT_HistogramData",
             3: "mwMDT_ImpedanceData",
             12: "mwMDT_LoadPullContour",
             11: "mwMDT_MultiTraceData",
             5: "mwMDT_NoiseData",
             1: "mwMDT_ReflectionData",
             9: "mwMDT_SourceMapData",
             8: "mwMDT_SpectrumData",
             6: "mwMDT_StabilityData",
             0: "mwMDT_UnKnown",
            }
    return items[value]


def mwModelCompatibilityVersion(value):
    items = {
             553: "mwMCV_Version553",
             600: "mwMCV_Version600",
             650: "mwMCV_Version650",
             750: "mwMCV_Version750",
             800: "mwMCV_Version800",
             900: "mwMCV_Version900",
            }
    return items[value]


def mwModelExtractType(value):
    items = {
             0: "mwMET_CircuitBasedModel",
             1: "mwMET_EMExtractedModel",
            }
    return items[value]


def mwModelParseType(value):
    items = {
             2: "mwMPT_AWRModel",
             1: "mwMPT_AWRNet",
             6: "mwMPT_HSPICE_native",
             5: "mwMPT_HSPICE_trans",
             3: "mwMPT_LibraModel",
             9: "mwMPT_MMICAD",
             4: "mwMPT_MWHarmModel",
             7: "mwMPT_PSpice",
             8: "mwMPT_Touchstone",
             0: "mwMPT_Unknown",
            }
    return items[value]


def mwModelPriorityType(value):
    items = {
             1: "mwMPT_ALL",
             9: "mwMPT_GROUND",
             8: "mwMPT_IO",
             10: "mwMPT_ISOLATED",
             3: "mwMPT_LINEAR",
             5: "mwMPT_MEAS",
             6: "mwMPT_NONLINEAR",
             11: "mwMPT_SINK",
             7: "mwMPT_SOURCE",
             4: "mwMPT_TUNEOPT",
             0: "mwMPT_UNINIT",
             2: "mwMPT_WIRE",
            }
    return items[value]


def mwModelPropertyFlags(value):
    items = {
             256: "mwEF_AggregateModel",
             2097152: "mwEF_AllowDuplicates",
             64: "mwEF_ConnectToSim",
             8192: "mwEF_DC_Source",
             0: "mwEF_Default",
             131072: "mwEF_DynamicModel",
             65536: "mwEF_ExtractBlock",
             8: "mwEF_IsDiodeModel",
             524288: "mwEF_ExtractedElement",
             4: "mwEF_HasNoiseModel",
             2048: "mwEF_HideModel",
             1: "mwEF_HideName",
             1048576: "mwEF_IncludeInTopOnly",
             16: "mwEF_IsBipolarModel",
             262144: "mwEF_IsDynamicRecord",
             1024: "mwEF_IsSysSimModel",
             32: "mwEF_Linear_or_NL",
             16384: "mwEF_MultiBranch",
             2: "mwEF_NamOnly",
             32768: "mwEF_NoAddIdInName",
             512: "mwEF_SpecSampleRate",
             4096: "mwEF_UseSimInstId",
             128: "mwEF_UseUniqueSim",
            }
    return items[value]


def mwNetViaMode(value):
    items = {
             0: "mwNVM_FullVias",
             2: "mwNVM_ManualVias",
             4: "mwNVM_Minimal2Vias",
             1: "mwNVM_MinimalVias",
             3: "mwNVM_SemiAutoVias",
            }
    return items[value]


def mwNetViaSizeOpts(value):
    items = {
             1: "mwVSO_ViaConversEntirePin",
             0: "mwVSO_ViaCoversPinRouteIntersection",
             2: "mwVSO_ViaMinimalSize",
            }
    return items[value]


def mwNetlistType(value):
    items = {
             0: "mwNLT_AWR",
             3: "mwNLT_HSPICE",
             10: "mwNLT_HSPICE2",
             4: "mwNLT_Native_HSPICE",
             7: "mwNLT_Native_APLAC",
             1: "mwNLT_SPICE",
             8: "mwNLT_Spectre",
             2: "mwNLT_Touchstone",
            }
    return items[value]


def mwNodeDataType(value):
    items = {
             3: "mwNDT_Complex",
             2: "mwNDT_Digital",
             4: "mwNDT_FixedPoint",
             1: "mwNDT_Real",
             0: "mwNDT_Unset",
            }
    return items[value]


def mwNodeFlags(value):
    items = {
             64: "mwNF_AllowDataTypeChange",
             2: "mwNF_BlockBuffer",
             0: "mwNF_Default",
             16: "mwNF_DispLabel",
             4: "mwNF_ModSignal",
             8: "mwNF_NoDigital",
             32: "mwNF_RFSignal",
             128: "mwNF_RW_BiDirection",
             1: "mwNF_Secondary",
            }
    return items[value]


def mwNodeType(value):
    items = {
             3: "mwNT_BiDirectional",
             0: "mwNT_Electrical",
             1: "mwNT_Input",
             2: "mwNT_Output",
            }
    return items[value]


def mwNonLinearSolveType(value):
    items = {
             2: "mwNLST_Direct",
             1: "mwNLST_Iterative",
             0: "mwNLST_Smart",
            }
    return items[value]


def mwObjectIncludeType(value):
    items = {
             1: "mwOIT_AllObjects",
             0: "mwOIT_SelectedObjects",
            }
    return items[value]


def mwObjectSelectFilters(value):
    items = {
             32: "mwOSF_Annotation",
             8192: "mwOSF_AreaPin",
             131072: "mwOSF_ArtworkCell",
             32768: "mwOSF_ByPositionFixed",
             2048: "mwOSF_BySize",
             65536: "mwOSF_BySize2",
             4096: "mwOSF_CellPort",
             8: "mwOSF_CommonElement",
             262144: "mwOSF_EMPort",
             524288: "mwOSF_EMSubCell",
             2: "mwOSF_Equation",
             1: "mwOSF_Graphics",
             768: "mwOSF_InstObject",
             256: "mwOSF_LayCell",
             1048576: "mwOSF_LayModifier",
             16384: "mwOSF_LayPort",
             128: "mwOSF_MovableProbe",
             0: "mwOSF_None",
             1024: "mwOSF_ParamFrame",
             28672: "mwOSF_PinObject",
             512: "mwOSF_SubCell",
             4: "mwOSF_Text",
             16: "mwOSF_Wire",
             64: "mwOSF_iNet",
            }
    return items[value]


def mwOptGoalType(value):
    items = {
             0: "mwOGT_Equals",
             2: "mwOGT_GreaterThan",
             1: "mwOGT_LessThan",
            }
    return items[value]


def mwOptimizerSetting(value):
    items = {
             101: "mwOS_MaxIterations",
             100: "mwOS_OptimizerSelected",
             103: "mwOS_Property",
             108: "mwOS_ResetYield",
             107: "mwOS_ResultsCleared",
             106: "mwOS_ResultsReverted",
             105: "mwOS_ResultsSaved",
             102: "mwOS_StopAtMin",
             109: "mwOS_StopOnErr",
             104: "mwOS_StopRequested",
            }
    return items[value]


def mwOutputFileLineEndFormat(value):
    items = {
             1: "mwOFE_DOSFormatLineEnd",
             0: "mwOFE_NormalLineEnd",
            }
    return items[value]


def mwOutputFilePortParameterFormat(value):
    items = {
             2: "mwOFF_DB_Magnitude_Angle",
             1: "mwOFF_Magnitude_Angle",
             0: "mwOFF_Real_Imaginary",
            }
    return items[value]


def mwOutputFilePortParameterFreqUnits(value):
    items = {
             3: "mwOFU_GHz",
             0: "mwOFU_Hz",
             2: "mwOFU_MHz",
             4: "mwOFU_THz",
             1: "mwOFU_kHz",
            }
    return items[value]


def mwOutputFilePortParameterType(value):
    items = {
             3: "mwOFP_GParameter",
             4: "mwOFP_HParameter",
             0: "mwOFP_SParameter",
             1: "mwOFP_YParameter",
             2: "mwOFP_ZParameter",
            }
    return items[value]


def mwPageSetupDetailLevel(value):
    items = {
             0: "mwPSD_MaximumVisability",
             1: "mwPSD_MinimumComplexity",
            }
    return items[value]


def mwPageSetupOrientation(value):
    items = {
             1: "mwPSO_Landscape",
             0: "mwPSO_Portrait",
            }
    return items[value]


def mwParamDefDataType(value):
    items = {
             1: "mwPDDT_Complex",
             5: "mwPDDT_DataModel",
             4: "mwPDDT_ElementName",
             8: "mwPDDT_Enumeration",
             10: "mwPDDT_FileName",
             6: "mwPDDT_InfoString",
             2: "mwPDDT_Integer",
             7: "mwPDDT_None",
             0: "mwPDDT_Real",
             9: "mwPDDT_RealVector",
             3: "mwPDDT_String",
            }
    return items[value]


def mwParameterDefinitionFlagType(value):
    items = {
             24: "mwPDF_Binned",
             8: "mwPDF_BoldFont",
             25: "mwPDF_ChangeConnectivity",
             20: "mwPDF_ChangeNotDirty",
             17: "mwPDF_ChangeStructural",
             16: "mwPDF_ConnectToSim",
             0: "mwPDF_Default",
             18: "mwPDF_DynamicModParam",
             6: "mwPDF_EmptyStringOk",
             1: "mwPDF_Hide",
             2: "mwPDF_HideIfEmpty",
             3: "mwPDF_HideUnits",
             7: "mwPDF_HideVarName",
             10: "mwPDF_IsPortNumber",
             4: "mwPDF_LJustify",
             27: "mwPDF_LayCell_EleParam",
             21: "mwPDF_NoAffectLayout",
             26: "mwPDF_NoDocNameSync",
             22: "mwPDF_NoTune",
             12: "mwPDF_NonStructural",
             15: "mwPDF_ParDefIsCopy",
             14: "mwPDF_ReadDataTable",
             5: "mwPDF_ReadOnly",
             9: "mwPDF_Secondary",
             19: "mwPDF_StreamParDef",
             13: "mwPDF_Structural",
             23: "mwPDF_Synthesized",
             11: "mwPDF_UniqueVectLength",
            }
    return items[value]


def mwParameterStyle(value):
    items = {
             5: "mwPS_BoldFont",
             0: "mwPS_Hide",
             2: "mwPS_HideEmpty",
             6: "mwPS_HideIfSecondary",
             1: "mwPS_HideUnits",
             3: "mwPS_HideVarName",
             4: "mwPS_LeftJustify",
            }
    return items[value]


def mwParameterStyleSetting(value):
    items = {
             1: "mwPSS_ClearStyle",
             0: "mwPSS_SetStyle",
             2: "mwPSS_UseDefaultStyle",
            }
    return items[value]


def mwPathAttributes(value):
    items = {
             8: "mwPA_Area",
             5: "mwPA_BeginExt",
             6: "mwPA_EndExt",
             0: "mwPA_LayerIndex",
             7: "mwPA_Length",
             3: "mwPA_MiterType",
             4: "mwPA_OffsetMiterAmount",
             2: "mwPA_PathEndType",
             1: "mwPA_PathWidth",
            }
    return items[value]


def mwPathEndType(value):
    items = {
             1: "mwPET_ExtendedHalfWidth",
             4: "mwPET_ExtendedUserDefined",
             2: "mwPET_Flush",
             3: "mwPET_Rounded",
             0: "mwPET_Various",
            }
    return items[value]


def mwPathEndTypeOptions(value):
    items = {
             0: "mwPETO_ExtendedHalfWidth",
             1: "mwPETO_FlushEnd",
             2: "mwPETO_Rounded",
            }
    return items[value]


def mwPathMiterType(value):
    items = {
             4: "mwPMT_Curved",
             2: "mwPMT_Mitered",
             3: "mwPMT_OffsetMitered",
             5: "mwPMT_Rounded",
             1: "mwPMT_Square",
             0: "mwPMT_Various",
            }
    return items[value]


def mwPathMiterTypeOptions(value):
    items = {
             1: "mwPMTO_Mitered",
             2: "mwPMTO_OffsetMiter",
             0: "mwPMTO_Square",
            }
    return items[value]


def mwPlacementJustfication(value):
    items = {
             0: "mwPJ_BBoxCenter",
             2: "mwPJ_BBoxLowerLeft",
             4: "mwPJ_BBoxLowerRight",
             1: "mwPJ_BBoxUpperLeft",
             3: "mwPJ_BBoxUpperRight",
             5: "mwPJ_SameOrigin",
            }
    return items[value]


def mwPlot3DGridAttributes(value):
    items = {
             13: "mwP3A_AutoDivisionsX",
             14: "mwP3A_AutoDivisionsY",
             15: "mwP3A_AutoDivisionsZ",
             29: "mwP3A_AutoRangeMaxX",
             31: "mwP3A_AutoRangeMaxY",
             33: "mwP3A_AutoRangeMaxZ",
             28: "mwP3A_AutoRangeMinX",
             30: "mwP3A_AutoRangeMinY",
             32: "mwP3A_AutoRangeMinZ",
             1: "mwP3A_AxisGridColorX",
             2: "mwP3A_AxisGridColorY",
             3: "mwP3A_AxisGridColorZ",
             4: "mwP3A_AxisLabelX",
             5: "mwP3A_AxisLabelY",
             6: "mwP3A_AxisLabelZ",
             34: "mwP3A_EnableLighting",
             38: "mwP3A_LightLevelAmbient",
             39: "mwP3A_LightLevelDiffuse",
             40: "mwP3A_LightLevelSpecular",
             41: "mwP3A_LightMaterialAmbient",
             42: "mwP3A_LightMaterialDiffuse",
             45: "mwP3A_LightMaterialEmission",
             44: "mwP3A_LightMaterialShininess",
             43: "mwP3A_LightMaterialSpecular",
             35: "mwP3A_LightPositionX",
             36: "mwP3A_LightPositionY",
             37: "mwP3A_LightPositionZ",
             10: "mwP3A_ManualDivisionsX",
             11: "mwP3A_ManualDivisionsY",
             12: "mwP3A_ManualDivisionsZ",
             23: "mwP3A_ManualRangeMaxX",
             25: "mwP3A_ManualRangeMaxY",
             27: "mwP3A_ManualRangeMaxZ",
             22: "mwP3A_ManualRangeMinX",
             24: "mwP3A_ManualRangeMinY",
             26: "mwP3A_ManualRangeMinZ",
             0: "mwP3A_None",
             16: "mwP3A_ShowDivisionValuesX",
             17: "mwP3A_ShowDivisionValuesY",
             18: "mwP3A_ShowDivisionValuesZ",
             47: "mwP3A_ShowUnitsLabelX",
             49: "mwP3A_ShowUnitsLabelY",
             7: "mwP3A_UseAutoDivisionsX",
             8: "mwP3A_UseAutoDivisionsY",
             9: "mwP3A_UseAutoDivisionsZ",
             19: "mwP3A_UseAutoRangeX",
             20: "mwP3A_UseAutoRangeY",
             21: "mwP3A_UseAutoRangeZ",
             46: "mwP3A_UseDefaultLabelX",
             48: "mwP3A_UseDefaultLabelY",
            }
    return items[value]


def mwPlotAxis(value):
    items = {
             0: "mwPA_Left",
             1: "mwPA_Right",
            }
    return items[value]


def mwPolarGridAttributes(value):
    items = {
             11: "mwPGA_AngleAutoDivisions",
             17: "mwPGA_AngleDivisions",
             9: "mwPGA_AngleLineStyle",
             18: "mwPGA_AngleSubdivisions",
             2: "mwPGA_DefaultSweepRange",
             5: "mwPGA_GraticuleColor",
             10: "mwPGA_MagniAutoDivisions",
             13: "mwPGA_MagnitudeDivisions",
             12: "mwPGA_MagnitudeLimit",
             8: "mwPGA_MagnitudeLineStyle",
             15: "mwPGA_MagnitudeMaximum",
             16: "mwPGA_MagnitudeMinimum",
             14: "mwPGA_MagnitudeSubdivisions",
             6: "mwPGA_MajorDivisionsColor",
             7: "mwPGA_MinorDivisionsColor",
             0: "mwPGA_None",
             1: "mwPGA_PolarChartStyle",
             22: "mwPGA_ShowAngDivisions",
             23: "mwPGA_ShowAngSubdivisions",
             24: "mwPGA_ShowAngValues",
             19: "mwPGA_ShowMagDivisions",
             20: "mwPGA_ShowMagSubdivisions",
             21: "mwPGA_ShowMagValues",
             4: "mwPGA_SweepDisplayMax",
             3: "mwPGA_SweepDisplayMin",
             26: "mwPGA_SweepMaximum",
             25: "mwPGA_SweepMinimum",
            }
    return items[value]


def mwPolygonAttributes(value):
    items = {
             1: "mwPOA_Area",
             0: "mwPOA_LayerIndex",
            }
    return items[value]


def mwPolylineAttributes(value):
    items = {
             0: "mwPLA_LayerIndex",
             1: "mwPLA_Length",
            }
    return items[value]


def mwPortFaceConnectTypes(value):
    items = {
             300: "mwCT_ArtworkLine",
             399: "mwCT_PassThroughBase",
             2: "mwCT_CapBotPlate",
             1: "mwCT_CapTopPlate",
             10: "mwCT_Disabled",
             100: "mwCT_LineEnd",
             199: "mwCT_LineEndN",
             200: "mwCT_LineJunction",
             299: "mwCT_LineJunctionN",
             400: "mwCT_PassThrough",
             499: "mwCT_PassThroughN",
             7: "mwCT_Resistor",
             8: "mwCT_Resistor2",
             9: "mwCT_Resistor3",
             3: "mwCT_SpiralExit",
             4: "mwCT_SpiralTurn",
             0: "mwCT_Unknown",
             6: "mwCT_ViaBottom",
             5: "mwCT_ViaTop",
            }
    return items[value]


def mwPrecisionMode(value):
    items = {
             1: "mwPM_Auto",
             2: "mwPM_Manual",
            }
    return items[value]


def mwPrecisionStyle(value):
    items = {
             2: "mwPS_FixedRightDecimal",
             1: "mwPS_FixedSigFigures",
             3: "mwPS_Scientific",
            }
    return items[value]


def mwPrintPaperSize(value):
    items = {
             44: "mwPPS_10X11",
             15: "mwPPS_10X14",
             16: "mwPPS_11X17",
             87: "mwPPS_12X11",
             45: "mwPPS_15X11",
             43: "mwPPS_9X11",
             63: "mwPPS_A2",
             7: "mwPPS_A3",
             60: "mwPPS_A3_Extra",
             65: "mwPPS_A3_Extra_Transverse",
             73: "mwPPS_A3_Rotated",
             64: "mwPPS_A3_Transverse",
             8: "mwPPS_A4",
             50: "mwPPS_A4_Extra",
             57: "mwPPS_A4_Plus",
             74: "mwPPS_A4_Rotated",
             9: "mwPPS_A4_SMALL",
             52: "mwPPS_A4_Transverse",
             10: "mwPPS_A5",
             61: "mwPPS_A5_Extra",
             75: "mwPPS_A5_Rotated",
             58: "mwPPS_A5_Transverse",
             67: "mwPPS_A6",
             80: "mwPPS_A6_Rotated",
             54: "mwPPS_A_Plus",
             11: "mwPPS_B4",
             76: "mwPPS_B4_JIS_Rotated",
             12: "mwPPS_B5",
             62: "mwPPS_B5_Extra",
             77: "mwPPS_B5_JIS_Rotated",
             59: "mwPPS_B5_Transverse",
             85: "mwPPS_B6_JIS",
             86: "mwPPS_B6_JIS_Rotated",
             55: "mwPPS_B_Plus",
             23: "mwPPS_CSheet",
             24: "mwPPS_DSheet",
             66: "mwPPS_Dbl_Japanese_Postcard",
             79: "mwPPS_Dbl_Japanese_Postcard_Rotated",
             25: "mwPPS_ESheet",
             19: "mwPPS_Env_10",
             20: "mwPPS_Env_11",
             21: "mwPPS_Env_12",
             22: "mwPPS_Env_14",
             18: "mwPPS_Env_9",
             32: "mwPPS_Env_B4",
             33: "mwPPS_Env_B5",
             34: "mwPPS_Env_B6",
             28: "mwPPS_Env_C3",
             29: "mwPPS_Env_C4",
             27: "mwPPS_Env_C5",
             30: "mwPPS_Env_C6",
             31: "mwPPS_Env_C65",
             26: "mwPPS_Env_DL",
             46: "mwPPS_Env_Invite",
             35: "mwPPS_Env_Italy",
             36: "mwPPS_Env_Monarch",
             37: "mwPPS_Env_Personal",
             6: "mwPPS_Executive",
             40: "mwPPS_Fanfold_Lgl_German",
             39: "mwPPS_Fanfold_Std_German",
             38: "mwPPS_Fanfold_US",
             13: "mwPPS_Folio",
             41: "mwPPS_ISO_B4",
             70: "mwPPS_JEnv_CHOU3",
             83: "mwPPS_JEnv_CHOU3_Rotated",
             71: "mwPPS_JEnv_CHOU4",
             84: "mwPPS_JEnv_CHOU4_Rotated",
             68: "mwPPS_JEnv_KAKU2",
             81: "mwPPS_JEnv_KAKU2_Rotated",
             69: "mwPPS_JEnv_KAKU3",
             82: "mwPPS_JEnv_KAKU3_Rotated",
             88: "mwPPS_JEnv_YOU4",
             89: "mwPPS_JEnv_YOU4_Rotated",
             42: "mwPPS_Japanese_Postcard",
             78: "mwPPS_Japanese_Postcard_Rotated",
             3: "mwPPS_Ledger",
             4: "mwPPS_Legal",
             48: "mwPPS_Legal_Extra",
             0: "mwPPS_Letter",
             1: "mwPPS_LetterSmall",
             47: "mwPPS_Letter_Extra",
             53: "mwPPS_Letter_Extra_Transverse",
             56: "mwPPS_Letter_Plus",
             72: "mwPPS_Letter_Rotated",
             51: "mwPPS_Letter_Transverse",
             17: "mwPPS_Note",
             90: "mwPPS_P16K",
             103: "mwPPS_P16K_Rotated",
             91: "mwPPS_P32K",
             92: "mwPPS_P32KBIG",
             105: "mwPPS_P32KBig_Rotated",
             104: "mwPPS_P32K_Rotated",
             93: "mwPPS_PEnv_1",
             102: "mwPPS_PEnv_10",
             115: "mwPPS_PEnv_10_Rotated",
             106: "mwPPS_PEnv_1_Rotated",
             94: "mwPPS_PEnv_2",
             107: "mwPPS_PEnv_2_Rotated",
             95: "mwPPS_PEnv_3",
             108: "mwPPS_PEnv_3_Rotated",
             96: "mwPPS_PEnv_4",
             109: "mwPPS_PEnv_4_Rotated",
             97: "mwPPS_PEnv_5",
             110: "mwPPS_PEnv_5_Rotated",
             98: "mwPPS_PEnv_6",
             111: "mwPPS_PEnv_6_Rotated",
             99: "mwPPS_PEnv_7",
             112: "mwPPS_PEnv_7_Rotated",
             100: "mwPPS_PEnv_8",
             113: "mwPPS_PEnv_8_Rotated",
             101: "mwPPS_PEnv_9",
             114: "mwPPS_PEnv_9_Rotated",
             14: "mwPPS_Quarto",
             5: "mwPPS_Statement",
             2: "mwPPS_Tabloid",
             49: "mwPPS_Tabloid_Extra",
            }
    return items[value]


def mwPrintPaperSource(value):
    items = {
             7: "mwPSR_Auto",
             6: "mwPSR_EnvManual",
             5: "mwPSR_Evelope",
             12: "mwPSR_FormSource",
             11: "mwPSR_LargeCapacity",
             10: "mwPSR_LargeFmt",
             2: "mwPSR_Lower",
             4: "mwPSR_Manual",
             3: "mwPSR_Middle",
             1: "mwPSR_OnlyOne",
             9: "mwPSR_SmallFmt",
             8: "mwPSR_Tractor",
             0: "mwPSR_Upper",
             13: "mwPSR_User",
            }
    return items[value]


def mwProjectItemType(value):
    items = {
             6: "mwPIT_Annotation",
             4: "mwPIT_DataFile",
             19: "mwPIT_DataSet",
             18: "mwPIT_DataSetFolder",
             11: "mwPIT_DesignNotes",
             2: "mwPIT_EMStructure",
             12: "mwPIT_GlobalDefinitions",
             5: "mwPIT_Graph",
             7: "mwPIT_Measurement",
             3: "mwPIT_Netlist",
             8: "mwPIT_OptimizerGoal",
             16: "mwPIT_Other",
             13: "mwPIT_OutputEquations",
             10: "mwPIT_OutputFile",
             17: "mwPIT_SampleProjectItem",
             0: "mwPIT_Schematic",
             1: "mwPIT_SystemDiagram",
             14: "mwPIT_Wizard",
             15: "mwPIT_WizardInstance",
             9: "mwPIT_YieldGoal",
            }
    return items[value]


def mwProjectTemplateType(value):
    items = {
             1: "mwPT_NormalTemplate",
            }
    return items[value]


def mwProjectToolFlags(value):
    items = {
             512: "mwPTF_AnchorTool",
             16: "mwPTF_AutoView",
             32768: "mwPTF_DRC",
             16384: "mwPTF_GridMult",
             1024: "mwPTF_Measure",
             2: "mwPTF_Redo",
             256: "mwPTF_SnapAll",
             128: "mwPTF_SnapToFit",
             64: "mwPTF_SnapTogether",
             32: "mwPTF_Tune",
             1: "mwPTF_Undo",
             8192: "mwPTF_View3D",
             4096: "mwPTF_ViewLayout",
             2048: "mwPTF_ViewSchematic",
             4: "mwPTF_ZoomArea",
             8: "mwPTF_ZoomOut",
            }
    return items[value]


def mwProjectVersionType(value):
    items = {
             1: "mwPV_Latest",
             2: "mwPV_Previous",
             3: "mwPV_VersionNumber",
            }
    return items[value]


def mwPropertyDataType(value):
    items = {
             0: "mwPDT_Boolean",
             1: "mwPDT_Byte",
             7: "mwPDT_Date",
             5: "mwPDT_Double",
             2: "mwPDT_Integer",
             3: "mwPDT_Long",
             4: "mwPDT_Single",
             6: "mwPDT_Text",
            }
    return items[value]


def mwRectGridAttributes(value):
    items = {
             11: "mwRGA_DefaultXLabel",
             2: "mwRGA_GraticuleColor",
             6: "mwRGA_LeftYAxisLineStyle",
             3: "mwRGA_MajorDivisionsColor",
             4: "mwRGA_MinorDivisionsColor",
             0: "mwRGA_None",
             1: "mwRGA_RectChartType",
             7: "mwRGA_RightYAxisLineStyle",
             8: "mwRGA_ShowTickMarks",
             9: "mwRGA_TickMarkSize",
             10: "mwRGA_UseDefaultXLabel",
             5: "mwRGA_XAxisLineStyle",
            }
    return items[value]


def mwRectangleAttributes(value):
    items = {
             0: "mwRA_LayerIndex",
            }
    return items[value]


def mwRouteBendStyleType(value):
    items = {
             2: "mwBS_CurveBendStyle",
             1: "mwBS_MiterBendStyle",
             0: "mwBS_SquareBendStyle",
            }
    return items[value]


def mwRouteConnModel(value):
    items = {
             2: "mwRCM_CenterLineAndAdjacentModel",
             1: "mwRCM_CenterlineConnectionModel",
             0: "mwRCM_UseProjectDefault",
            }
    return items[value]


def mwRouteObjectType(value):
    items = {
             2: "mwROT_GuideRouteObject",
             0: "mwROT_PathRouteObject",
             1: "mwROT_ViaRouteObject",
            }
    return items[value]


def mwRouteObstructionLevel(value):
    items = {
             2: "mwROL_AvoidObjstructions",
             1: "mwROL_IgnoreExistingNets",
             0: "mwROL_IgnoreObstructions",
            }
    return items[value]


def mwRouteSegmentEndOffsetType(value):
    items = {
             2: "mwEOS_ExtendedEndOffsetType",
             1: "mwEOS_FlushEndOffsetType",
             0: "mwEOS_NormalEndOffsetType",
            }
    return items[value]


def mwRouteSegmentEndStyleType(value):
    items = {
             3: "mwEST_ChamferEndStyle",
             4: "mwEST_CustomEndStyle",
             1: "mwEST_ExtendedEndStyle",
             5: "mwEST_RoundedEndStyle",
             0: "mwEST_TruncateEndStyle",
             2: "mwEST_VariableEndStyle",
            }
    return items[value]


def mwRouteStatusType(value):
    items = {
             1: "mwRST_FixedRouteStatus",
             2: "mwRST_LockedRouteStatus",
             0: "mwRST_NormalRouteStatus",
            }
    return items[value]


def mwRouteTopologyType(value):
    items = {
             7: "mwRTT_BlockRingRouteTopology",
             4: "mwRTT_BlockWireRouteTopology",
             8: "mwRTT_CoreWireRouteTopology",
             3: "mwRTT_IOWireRouteTopology",
             0: "mwRTT_NoneRouteTopology",
             6: "mwRTT_PadRingRouteTopology",
             5: "mwRTT_RingRouteTopology",
             2: "mwRTT_StandardCellWireRouteTopology",
             1: "mwRTT_StripeRouteTopology",
            }
    return items[value]


def mwRouteViaDirectionType(value):
    items = {
             0: "mwVDT_Layer1ToLayer2ViaDirection",
             1: "mwVDT_Layer2ToLayer1ViaDirection",
            }
    return items[value]


def mwScaleType(value):
    items = {
             1: "mwScaleLinear",
             2: "mwScaleLogarithmic",
            }
    return items[value]


def mwSchematicExportFormat(value):
    items = {
             0: "mwSEF_MWOSchematicFile",
            }
    return items[value]


def mwSchematicFontAttributes(value):
    items = {
             1: "mwSFA_BoldStyle",
             3: "mwSFA_FontHeight",
             0: "mwSFA_FontName",
             2: "mwSFA_ItalicStyle",
            }
    return items[value]


def mwSchematicNetlistExportFormat(value):
    items = {
             0: "mwNEF_MWONetlistFile",
            }
    return items[value]


def mwShapeArcDirection(value):
    items = {
             1: "mwSAD_Clockwise",
             0: "mwSAD_CounterClockwise",
            }
    return items[value]


def mwShapeModifierPriority(value):
    items = {
             2: "mwSMP_FlattenShape",
             3: "mwSMP_GlobalModifier",
             1: "mwSMP_NormalShape",
             4: "mwSMP_ShapeProcessor",
            }
    return items[value]


def mwShapeModifierType(value):
    items = {
             1: "mwMD_GlobalModifier",
             0: "mwMD_ShapeModifier",
            }
    return items[value]


def mwShapeNetType(value):
    items = {
             0: "mwSNT_Normal",
            }
    return items[value]


def mwShapePreprocessorAttributes(value):
    items = {
             0: "mwSPA_PreprocessorRules",
            }
    return items[value]


def mwShapeSubObjectType(value):
    items = {
             1: "mwSSO_CutoutCircle",
             2: "mwSSO_CutoutEllipse",
             0: "mwSSO_CutoutPolygon",
            }
    return items[value]


def mwShapeToolFlags(value):
    items = {
             16384: "mwSTF_ArrayCopy",
             524288: "mwSTF_DimLine",
             2048: "mwSTF_DrillHole",
             8: "mwSTF_Ellipse",
             4096: "mwSTF_Group",
             16: "mwSTF_Intersect",
             4: "mwSTF_Path",
             2: "mwSTF_Polygon",
             1: "mwSTF_Rectangle",
             256: "mwSTF_Resize",
             512: "mwSTF_ResizeCopy",
             1024: "mwSTF_Ring",
             262144: "mwSTF_Ruler",
             65536: "mwSTF_Sliced",
             32768: "mwSTF_StretchArea",
             64: "mwSTF_Subtract",
             131072: "mwSTF_Text",
             8192: "mwSTF_UnGroup",
             32: "mwSTF_Union",
             128: "mwSTF_Xor",
            }
    return items[value]


def mwShapeType(value):
    items = {
             8: "mwST_Arc",
             7: "mwST_CellStretcher",
             5: "mwST_DrillHole",
             3: "mwST_Ellipse",
             2: "mwST_Path",
             9: "mwST_Pin",
             1: "mwST_Polygon",
             10: "mwST_Polyline",
             6: "mwST_Port",
             0: "mwST_Rectangle",
             4: "mwST_Text",
            }
    return items[value]


def mwShowFileFlags(value):
    items = {
             32: "mwSFF_AUTOUPDATE",
             64: "mwSFF_FILEBUFFER",
             16: "mwSFF_USEEXPLORER",
            }
    return items[value]


def mwShowFileType(value):
    items = {
             0: "mwSFT_PlainText",
             1: "mwSFT_RichText",
            }
    return items[value]


def mwSimStateFlags(value):
    items = {
             16: "mwSSF_NeedsUpdate",
             8: "mwSSF_ParameterDirty",
             0: "mwSSF_SimClean",
             2: "mwSSF_SimFrequencyDirty",
             1: "mwSSF_SimStructureDirty",
            }
    return items[value]


def mwSmithGridAttributes(value):
    items = {
             14: "mwSGA_AdmittanceColor",
             6: "mwSGA_AdmittanceGridVisible",
             16: "mwSGA_AdmittanceLineStyle",
             10: "mwSGA_AutoContour",
             8: "mwSGA_AutoSize",
             9: "mwSGA_ChartSize",
             11: "mwSGA_ContourDensity",
             2: "mwSGA_DefaultSweepRange",
             12: "mwSGA_GraticuleColor",
             13: "mwSGA_ImpedanceColor",
             5: "mwSGA_ImpedanceGridVisible",
             15: "mwSGA_ImpedanceLineStyle",
             0: "mwSGA_None",
             1: "mwSGA_SmithChartStyle",
             4: "mwSGA_SweepDisplayMax",
             3: "mwSGA_SweepDisplayMin",
             18: "mwSGA_SweepMaximum",
             17: "mwSGA_SweepMinimum",
             7: "mwSGA_ValuesVisible",
            }
    return items[value]


def mwSpiceExtractionModelLevel(value):
    items = {
             1: "mwSML_1stOrder",
             2: "mwSML_2ndOrder",
             3: "mwSML_Distributed",
             4: "mwSML_MostAccurate",
             0: "mwSML_Simplest",
            }
    return items[value]


def mwStatisticalDist(value):
    items = {
             0: "mwSD_Deterministic",
             5: "mwSD_Discrete",
             4: "mwSD_LogNormal",
             3: "mwSD_ModelDist",
             7: "mwSD_NormalClipped",
             2: "mwSD_NormalDist",
             6: "mwSD_NormalMinusTol",
             1: "mwSD_UniformDist",
            }
    return items[value]


def mwStatusItemCategory(value):
    items = {
             0: "mwRIC_Error",
             2: "mwRIC_Info",
             1: "mwRIC_Warning",
            }
    return items[value]


def mwSubcktGroundType(value):
    items = {
             2: "mwSG_Balanced",
             1: "mwSG_Explicit",
             0: "mwSG_Normal",
            }
    return items[value]


def mwSymbolPathAttributes(value):
    items = {
             3: "mwSPA_MiterOffset",
             2: "mwSPA_MiterType",
             1: "mwSPA_Width",
             5: "mwSPA_bOffset",
             6: "mwSPA_eOffset",
             4: "mwSPA_endType",
            }
    return items[value]


def mwSymbolSelectMode(value):
    items = {
             1: "mwSM_EdgeSelect",
             0: "mwSM_NormalSelect",
            }
    return items[value]


def mwSymbolShapeType(value):
    items = {
             1: "mwSST_Arc",
             5: "mwSST_Ellipse",
             0: "mwSST_Line",
             8: "mwSST_MetaText",
             6: "mwSST_Node",
             3: "mwSST_Path",
             2: "mwSST_Polygon",
             7: "mwSST_Polyline",
             4: "mwSST_Text",
            }
    return items[value]


def mwSymbolTextAttributes(value):
    items = {
             5: "mwSTA_Font",
             1: "mwSTA_Height",
             3: "mwSTA_Rotation",
             4: "mwSTA_Text",
             2: "mwSTA_Width",
            }
    return items[value]


def mwSymbolType(value):
    items = {
             1: "mwST_ProjectSymbolType",
             0: "mwST_SystemSymbolType",
            }
    return items[value]


def mwSysNoiseModeling(value):
    items = {
             0: "mwSNM_Noiseless",
             2: "mwSNM_RFBudgetAndTimeDomain",
             1: "mwSNM_RFBudgetOnly",
            }
    return items[value]


def mwSystemExportFormat(value):
    items = {
             0: "mwSYF_MWOSystemFile",
            }
    return items[value]


def mwSystemSimulatorState(value):
    items = {
             2: "mwSSS_Paused",
             1: "mwSSS_Running",
             3: "mwSSS_Starting",
             0: "mwSSS_Stopped",
            }
    return items[value]


def mwTabularGridAttributes(value):
    items = {
             3: "mwTGA_DataPrecision",
             2: "mwTGA_DisplayFormat",
             0: "mwTGA_None",
             1: "mwTGA_NumberFormat",
             4: "mwTGA_SweepPrecision",
            }
    return items[value]


def mwTextAlignment(value):
    items = {
             8: "mwTAl_BottomCenter",
             7: "mwTAl_BottomLeft",
             9: "mwTAl_BottomRight",
             5: "mwTAl_CenterCenter",
             4: "mwTAl_CenterLeft",
             6: "mwTAl_CenterRight",
             2: "mwTAl_TopCenter",
             1: "mwTAl_TopLeft",
             3: "mwTAl_TopRight",
            }
    return items[value]


def mwThickness(value):
    items = {
             5: "mwFat",
             1: "mwHairline",
             3: "mwMedium",
             4: "mwThick",
             2: "mwThin",
            }
    return items[value]


def mwTraceSteppedColorStyle(value):
    items = {
             3: "mwSteppedColorStyleGradient",
             6: "mwSteppedColorStyleGradientBlue",
             5: "mwSteppedColorStyleGradientGreen",
             4: "mwSteppedColorStyleGradientRed",
             1: "mwSteppedColorStyleNone",
             7: "mwSteppedColorStyleShaded",
             2: "mwSteppedColorStyleStepped",
            }
    return items[value]


def mwTraceStyle(value):
    items = {
             1: "mwTraceStyleAuto",
             6: "mwTraceStyleDigital",
             5: "mwTraceStyleHistogram",
             2: "mwTraceStyleLinear",
             7: "mwTraceStyleSampled",
             3: "mwTraceStyleScatter",
             4: "mwTraceStyleSpectral",
             8: "mwTraceStyleVariationBars",
            }
    return items[value]


def mwTraceSymbols(value):
    items = {
             9: "mwSymbolArrow",
             8: "mwSymbolBackSlash",
             10: "mwSymbolCircle",
             12: "mwSymbolCross",
             3: "mwSymbolDiamond",
             7: "mwSymbolForwardSlash",
             5: "mwSymbolHorizontalBar",
             4: "mwSymbolRomanX",
             11: "mwSymbolSmallX",
             2: "mwSymbolSquare",
             1: "mwSymbolTriangle",
             6: "mwSymbolVerticalBar",
            }
    return items[value]


def mwUnionShapesType(value):
    items = {
             0: "mwUST_UnionOnExistingLayers",
             1: "mwUST_UnionToDestinationLayer",
            }
    return items[value]


def mwUnitMultType(value):
    items = {
             19: "mwUMT_Deg",
             15: "mwUMT_DegC",
             17: "mwUMT_DegF",
             16: "mwUMT_DegK",
             9: "mwUMT_Giga",
             8: "mwUMT_Mega",
             18: "mwUMT_Rad",
             10: "mwUMT_Tera",
             5: "mwUMT_c",
             20: "mwUMT_dbm",
             21: "mwUMT_dbw",
             0: "mwUMT_f",
             13: "mwUMT_feet",
             12: "mwUMT_inch",
             7: "mwUMT_k",
             4: "mwUMT_m",
             11: "mwUMT_mil",
             14: "mwUMT_mile",
             2: "mwUMT_n",
             6: "mwUMT_none",
             1: "mwUMT_p",
             3: "mwUMT_u",
            }
    return items[value]


def mwUnitType(value):
    items = {
             9: "mwUT_Angle",
             2: "mwUT_Capacitance",
             5: "mwUT_Conductance",
             12: "mwUT_Current",
             15: "mwUT_DB",
             18: "mwUT_DBOnlyPower",
             1: "mwUT_Frequency",
             3: "mwUT_Inductance",
             6: "mwUT_Length",
             7: "mwUT_LengthEnglish",
             0: "mwUT_None",
             14: "mwUT_Power",
             13: "mwUT_PowerLog",
             4: "mwUT_Resistance",
             17: "mwUT_Scaler",
             16: "mwUT_String",
             8: "mwUT_Temperature",
             20: "mwUT_TextOnly",
             10: "mwUT_Time",
             11: "mwUT_Voltage",
             19: "mwUT_WattsOnlyPower",
            }
    return items[value]


def mwVarPropMode(value):
    items = {
             0: "mwVPM_None",
             2: "mwVPM_Strong",
             1: "mwVPM_Weak",
            }
    return items[value]


def mwViaAlignType(value):
    items = {
             1: "mwVAT_ConstantClearance",
             0: "mwVAT_ConstantSpacing",
            }
    return items[value]


def mwViaFillStaggerMode(value):
    items = {
             2: "mwVSM_StaggerColumns",
             0: "mwVSM_StaggerNone",
             1: "mwVSM_StaggerRows",
            }
    return items[value]


def mwViaSpacingType(value):
    items = {
             0: "mwVST_CenterToCenter",
             1: "mwVST_EdgeToEdge",
            }
    return items[value]


def mwViewAutoRotate(value):
    items = {
             2: "mwVAW_RotateChangeSlope",
             0: "mwVAW_RotateNone",
             1: "mwVAW_RotateNormal",
            }
    return items[value]


def mwViewFrom(value):
    items = {
             3: "mwVF_Back",
             6: "mwVF_Bottom",
             2: "mwVF_Front",
             4: "mwVF_Left",
             7: "mwVF_None",
             0: "mwVF_Ortho",
             5: "mwVF_Right",
             1: "mwVF_Top",
            }
    return items[value]


def mwViewVisiual(value):
    items = {
             16: "mwVV_AntiAliased",
             32: "mwVV_ExtrudedOnly",
             2: "mwVV_Shaded",
             64: "mwVV_ShapesMerged",
             128: "mwVV_ShapesSelected",
             4: "mwVV_ShowEdges",
             256: "mwVV_Stippling",
             8: "mwVV_Texturing",
             1: "mwVV_WireFrame",
            }
    return items[value]


def mwWindowState(value):
    items = {
             1: "mwWS_Maximized",
             2: "mwWS_Minimized",
             3: "mwWS_Normal",
            }
    return items[value]


def mwWindowTileDirection(value):
    items = {
             0: "mwWTD_Horizontal",
             1: "mwWTD_Vertical",
            }
    return items[value]


def mwWindowType(value):
    items = {
             1: "mwWT_Datafile",
             2: "mwWT_DesignNotes",
             20: "mwWT_EmLayoutG3DStructure",
             17: "mwWT_EmLayoutStructure",
             18: "mwWT_EmLayoutStructure3D",
             19: "mwWT_EmLayoutStructureSchematic",
             3: "mwWT_EmStructure",
             4: "mwWT_EmStructure3D",
             7: "mwWT_GlobalEquation",
             5: "mwWT_Graph",
             16: "mwWT_LayoutCell",
             6: "mwWT_NetList",
             15: "mwWT_Optimizer",
             8: "mwWT_OutputEquation",
             9: "mwWT_Schematic",
             11: "mwWT_Schematic3DLayout",
             10: "mwWT_SchematicLayout",
             12: "mwWT_SystemDiagram",
             14: "mwWT_SystemDiagram3DLayout",
             13: "mwWT_SystemDiagramLayout",
             0: "mwWT_Unknown",
            }
    return items[value]


def mwYieldGoalType(value):
    items = {
             1: "mwYGT_GreaterThan",
             0: "mwYGT_LessThan",
            }
    return items[value]
