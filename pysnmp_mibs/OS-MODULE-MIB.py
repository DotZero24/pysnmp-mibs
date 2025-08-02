_Q='osModuleOptGroup'
_P='osModuleGroup'
_O='osModuleNfvCaps'
_N='osModuleMaxApn'
_M='osModCapLinkProtectionRev'
_L='osModuleWirelessCaps'
_K='osModuleGlobalCaps'
_J='osModuleDescription'
_I='osModuleAction'
_H='osModuleType'
_G='osModuleSupport'
_F='DisplayString'
_E='Integer32'
_D='Bits'
_C='read-only'
_B='current'
_A='OS-MODULE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
osModule=ModuleIdentity((1,3,6,1,4,1,6926,2,44))
if mibBuilder.loadTexts:osModule.setRevisions(('2022-07-13 00:00','2022-06-08 00:00','2022-06-06 00:00'))
_OsModuleGen_ObjectIdentity=ObjectIdentity
osModuleGen=_OsModuleGen_ObjectIdentity((1,3,6,1,4,1,6926,2,44,1))
class _OsModuleSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OsModuleSupport_Type.__name__=_E
_OsModuleSupport_Object=MibScalar
osModuleSupport=_OsModuleSupport_Object((1,3,6,1,4,1,6926,2,44,1,1),_OsModuleSupport_Type())
osModuleSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleSupport.setStatus(_B)
class _OsModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('empty',0),('unknown',1),('vdsl',2),('lte',3),('nfv',4),('nfvLte',5),('fiveG',6)))
_OsModuleType_Type.__name__=_E
_OsModuleType_Object=MibScalar
osModuleType=_OsModuleType_Object((1,3,6,1,4,1,6926,2,44,1,2),_OsModuleType_Type())
osModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleType.setStatus(_B)
class _OsModuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('modemReset',1)))
_OsModuleAction_Type.__name__=_E
_OsModuleAction_Object=MibScalar
osModuleAction=_OsModuleAction_Object((1,3,6,1,4,1,6926,2,44,1,3),_OsModuleAction_Type())
osModuleAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:osModuleAction.setStatus(_B)
class _OsModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_OsModuleDescription_Type.__name__=_F
_OsModuleDescription_Object=MibScalar
osModuleDescription=_OsModuleDescription_Object((1,3,6,1,4,1,6926,2,44,1,4),_OsModuleDescription_Type())
osModuleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleDescription.setStatus(_B)
_OsModuleCapabilities_ObjectIdentity=ObjectIdentity
osModuleCapabilities=_OsModuleCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,44,2))
_OsModCapGlobal_ObjectIdentity=ObjectIdentity
osModCapGlobal=_OsModCapGlobal_ObjectIdentity((1,3,6,1,4,1,6926,2,44,2,1))
class _OsModuleGlobalCaps_Type(Bits):namedValues=NamedValues(*(('capWireless',0),('capNfv',1)))
_OsModuleGlobalCaps_Type.__name__=_D
_OsModuleGlobalCaps_Object=MibScalar
osModuleGlobalCaps=_OsModuleGlobalCaps_Object((1,3,6,1,4,1,6926,2,44,2,1,1),_OsModuleGlobalCaps_Type())
osModuleGlobalCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleGlobalCaps.setStatus(_B)
_OsModCapWirelesslCom_ObjectIdentity=ObjectIdentity
osModCapWirelesslCom=_OsModCapWirelesslCom_ObjectIdentity((1,3,6,1,4,1,6926,2,44,2,2))
class _OsModuleWirelessCaps_Type(Bits):namedValues=NamedValues(*(('capLinkProtection',0),('capMobileAccess',1),('capFourG',2),('capFiveG',3)))
_OsModuleWirelessCaps_Type.__name__=_D
_OsModuleWirelessCaps_Object=MibScalar
osModuleWirelessCaps=_OsModuleWirelessCaps_Object((1,3,6,1,4,1,6926,2,44,2,2,1),_OsModuleWirelessCaps_Type())
osModuleWirelessCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleWirelessCaps.setStatus(_B)
class _OsModCapLinkProtectionRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,63))
_OsModCapLinkProtectionRev_Type.__name__=_F
_OsModCapLinkProtectionRev_Object=MibScalar
osModCapLinkProtectionRev=_OsModCapLinkProtectionRev_Object((1,3,6,1,4,1,6926,2,44,2,2,3),_OsModCapLinkProtectionRev_Type())
osModCapLinkProtectionRev.setMaxAccess(_C)
if mibBuilder.loadTexts:osModCapLinkProtectionRev.setStatus(_B)
_OsModuleMaxApn_Type=Unsigned32
_OsModuleMaxApn_Object=MibScalar
osModuleMaxApn=_OsModuleMaxApn_Object((1,3,6,1,4,1,6926,2,44,2,2,4),_OsModuleMaxApn_Type())
osModuleMaxApn.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleMaxApn.setStatus(_B)
_OsModCapNFV_ObjectIdentity=ObjectIdentity
osModCapNFV=_OsModCapNFV_ObjectIdentity((1,3,6,1,4,1,6926,2,44,2,3))
class _OsModuleNfvCaps_Type(Bits):namedValues=NamedValues(*(('capSingleIP',0),('capPCIe',1)))
_OsModuleNfvCaps_Type.__name__=_D
_OsModuleNfvCaps_Object=MibScalar
osModuleNfvCaps=_OsModuleNfvCaps_Object((1,3,6,1,4,1,6926,2,44,2,3,1),_OsModuleNfvCaps_Type())
osModuleNfvCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:osModuleNfvCaps.setStatus(_B)
_OsModConformance_ObjectIdentity=ObjectIdentity
osModConformance=_OsModConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,44,100))
_OsModMIBCompliances_ObjectIdentity=ObjectIdentity
osModMIBCompliances=_OsModMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,44,100,1))
_OsModMIBGroups_ObjectIdentity=ObjectIdentity
osModMIBGroups=_OsModMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,44,100,2))
osModuleGroup=ObjectGroup((1,3,6,1,4,1,6926,2,44,100,2,1))
osModuleGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:osModuleGroup.setStatus(_B)
osModuleOptGroup=ObjectGroup((1,3,6,1,4,1,6926,2,44,100,2,2))
osModuleOptGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:osModuleOptGroup.setStatus(_B)
osModuleMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,44,100,1,1))
osModuleMIBCompliance.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:osModuleMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'osModule':osModule,'osModuleGen':osModuleGen,_G:osModuleSupport,_H:osModuleType,_I:osModuleAction,_J:osModuleDescription,'osModuleCapabilities':osModuleCapabilities,'osModCapGlobal':osModCapGlobal,_K:osModuleGlobalCaps,'osModCapWirelesslCom':osModCapWirelesslCom,_L:osModuleWirelessCaps,_M:osModCapLinkProtectionRev,_N:osModuleMaxApn,'osModCapNFV':osModCapNFV,_O:osModuleNfvCaps,'osModConformance':osModConformance,'osModMIBCompliances':osModMIBCompliances,'osModuleMIBCompliance':osModuleMIBCompliance,'osModMIBGroups':osModMIBGroups,_P:osModuleGroup,_Q:osModuleOptGroup})