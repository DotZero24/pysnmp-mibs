_V='lldpXdot1EvbGroup'
_U='lldpV2Xdot1RemCdcpTlvString'
_T='lldpV2Xdot1RemEvbTlvString'
_S='lldpV2Xdot1LocCdcpTlvString'
_R='lldpV2Xdot1LocEvbTlvString'
_Q='lldpXdot1EvbConfigCdcpTxEnable'
_P='lldpXdot1EvbConfigEvbTxEnable'
_O='lldpXdot1EvbConfigCdcpEntry'
_N='lldpXdot1EvbConfigEvbEntry'
_M='read-write'
_L='ifGeneralInformationGroup'
_K='TruthValue'
_J='lldpV2RemTimeMark'
_I='lldpV2RemLocalIfIndex'
_H='lldpV2RemLocalDestMACAddress'
_G='lldpV2RemIndex'
_F='lldpV2LocPortIfIndex'
_E='read-only'
_D='OctetString'
_C='LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB'
_B='LLDP-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifGeneralInformationGroup,=mibBuilder.importSymbols('IF-MIB',_L)
lldpV2Xdot1MIB,=mibBuilder.importSymbols('LLDP-EXT-DOT1-V2-MIB','lldpV2Xdot1MIB')
lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_B,_F,'lldpV2PortConfigEntry',_G,_H,_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
lldpXDot1EvbExtensions=ModuleIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1))
if mibBuilder.loadTexts:lldpXDot1EvbExtensions.setRevisions(('2018-06-21 00:00','2014-12-15 00:00','2012-02-15 00:00'))
_LldpXdot1StandAloneExtensions_ObjectIdentity=ObjectIdentity
lldpXdot1StandAloneExtensions=_LldpXdot1StandAloneExtensions_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7))
_LldpXdot1EvbMIB_ObjectIdentity=ObjectIdentity
lldpXdot1EvbMIB=_LldpXdot1EvbMIB_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,1))
_LldpXdot1EvbObjects_ObjectIdentity=ObjectIdentity
lldpXdot1EvbObjects=_LldpXdot1EvbObjects_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1))
_LldpXdot1EvbConfig_ObjectIdentity=ObjectIdentity
lldpXdot1EvbConfig=_LldpXdot1EvbConfig_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1))
_LldpXdot1EvbConfigEvbTable_Object=MibTable
lldpXdot1EvbConfigEvbTable=_LldpXdot1EvbConfigEvbTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1EvbConfigEvbTable.setStatus(_A)
_LldpXdot1EvbConfigEvbEntry_Object=MibTableRow
lldpXdot1EvbConfigEvbEntry=_LldpXdot1EvbConfigEvbEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1EvbConfigEvbEntry.setStatus(_A)
class _LldpXdot1EvbConfigEvbTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1EvbConfigEvbTxEnable_Type.__name__=_K
_LldpXdot1EvbConfigEvbTxEnable_Object=MibTableColumn
lldpXdot1EvbConfigEvbTxEnable=_LldpXdot1EvbConfigEvbTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,1,1,1),_LldpXdot1EvbConfigEvbTxEnable_Type())
lldpXdot1EvbConfigEvbTxEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXdot1EvbConfigEvbTxEnable.setStatus(_A)
_LldpXdot1EvbConfigCdcpTable_Object=MibTable
lldpXdot1EvbConfigCdcpTable=_LldpXdot1EvbConfigCdcpTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,2))
if mibBuilder.loadTexts:lldpXdot1EvbConfigCdcpTable.setStatus(_A)
_LldpXdot1EvbConfigCdcpEntry_Object=MibTableRow
lldpXdot1EvbConfigCdcpEntry=_LldpXdot1EvbConfigCdcpEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,2,1))
if mibBuilder.loadTexts:lldpXdot1EvbConfigCdcpEntry.setStatus(_A)
class _LldpXdot1EvbConfigCdcpTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1EvbConfigCdcpTxEnable_Type.__name__=_K
_LldpXdot1EvbConfigCdcpTxEnable_Object=MibTableColumn
lldpXdot1EvbConfigCdcpTxEnable=_LldpXdot1EvbConfigCdcpTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,1,2,1,1),_LldpXdot1EvbConfigCdcpTxEnable_Type())
lldpXdot1EvbConfigCdcpTxEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXdot1EvbConfigCdcpTxEnable.setStatus(_A)
_LldpXdot1EvbLocalData_ObjectIdentity=ObjectIdentity
lldpXdot1EvbLocalData=_LldpXdot1EvbLocalData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2))
_LldpV2Xdot1LocEvbTlvTable_Object=MibTable
lldpV2Xdot1LocEvbTlvTable=_LldpV2Xdot1LocEvbTlvTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,1))
if mibBuilder.loadTexts:lldpV2Xdot1LocEvbTlvTable.setStatus(_A)
_LldpV2Xdot1LocEvbTlvEntry_Object=MibTableRow
lldpV2Xdot1LocEvbTlvEntry=_LldpV2Xdot1LocEvbTlvEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,1,1))
lldpV2Xdot1LocEvbTlvEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lldpV2Xdot1LocEvbTlvEntry.setStatus(_A)
class _LldpV2Xdot1LocEvbTlvString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,514))
_LldpV2Xdot1LocEvbTlvString_Type.__name__=_D
_LldpV2Xdot1LocEvbTlvString_Object=MibTableColumn
lldpV2Xdot1LocEvbTlvString=_LldpV2Xdot1LocEvbTlvString_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,1,1,1),_LldpV2Xdot1LocEvbTlvString_Type())
lldpV2Xdot1LocEvbTlvString.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2Xdot1LocEvbTlvString.setStatus(_A)
_LldpV2Xdot1LocCdcpTlvTable_Object=MibTable
lldpV2Xdot1LocCdcpTlvTable=_LldpV2Xdot1LocCdcpTlvTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,2))
if mibBuilder.loadTexts:lldpV2Xdot1LocCdcpTlvTable.setStatus(_A)
_LldpV2Xdot1LocCdcpTlvEntry_Object=MibTableRow
lldpV2Xdot1LocCdcpTlvEntry=_LldpV2Xdot1LocCdcpTlvEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,2,1))
lldpV2Xdot1LocCdcpTlvEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lldpV2Xdot1LocCdcpTlvEntry.setStatus(_A)
class _LldpV2Xdot1LocCdcpTlvString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,514))
_LldpV2Xdot1LocCdcpTlvString_Type.__name__=_D
_LldpV2Xdot1LocCdcpTlvString_Object=MibTableColumn
lldpV2Xdot1LocCdcpTlvString=_LldpV2Xdot1LocCdcpTlvString_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,2,2,1,1),_LldpV2Xdot1LocCdcpTlvString_Type())
lldpV2Xdot1LocCdcpTlvString.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2Xdot1LocCdcpTlvString.setStatus(_A)
_LldpXdot1EvbRemoteData_ObjectIdentity=ObjectIdentity
lldpXdot1EvbRemoteData=_LldpXdot1EvbRemoteData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3))
_LldpV2Xdot1RemEvbTlvTable_Object=MibTable
lldpV2Xdot1RemEvbTlvTable=_LldpV2Xdot1RemEvbTlvTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,1))
if mibBuilder.loadTexts:lldpV2Xdot1RemEvbTlvTable.setStatus(_A)
_LldpV2Xdot1RemEvbTlvEntry_Object=MibTableRow
lldpV2Xdot1RemEvbTlvEntry=_LldpV2Xdot1RemEvbTlvEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,1,1))
lldpV2Xdot1RemEvbTlvEntry.setIndexNames((0,_B,_J),(0,_B,_I),(0,_B,_H),(0,_B,_G))
if mibBuilder.loadTexts:lldpV2Xdot1RemEvbTlvEntry.setStatus(_A)
class _LldpV2Xdot1RemEvbTlvString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,514))
_LldpV2Xdot1RemEvbTlvString_Type.__name__=_D
_LldpV2Xdot1RemEvbTlvString_Object=MibTableColumn
lldpV2Xdot1RemEvbTlvString=_LldpV2Xdot1RemEvbTlvString_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,1,1,1),_LldpV2Xdot1RemEvbTlvString_Type())
lldpV2Xdot1RemEvbTlvString.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2Xdot1RemEvbTlvString.setStatus(_A)
_LldpV2Xdot1RemCdcpTlvTable_Object=MibTable
lldpV2Xdot1RemCdcpTlvTable=_LldpV2Xdot1RemCdcpTlvTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,2))
if mibBuilder.loadTexts:lldpV2Xdot1RemCdcpTlvTable.setStatus(_A)
_LldpV2Xdot1RemCdcpTlvEntry_Object=MibTableRow
lldpV2Xdot1RemCdcpTlvEntry=_LldpV2Xdot1RemCdcpTlvEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,2,1))
lldpV2Xdot1RemCdcpTlvEntry.setIndexNames((0,_B,_J),(0,_B,_I),(0,_B,_H),(0,_B,_G))
if mibBuilder.loadTexts:lldpV2Xdot1RemCdcpTlvEntry.setStatus(_A)
class _LldpV2Xdot1RemCdcpTlvString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,514))
_LldpV2Xdot1RemCdcpTlvString_Type.__name__=_D
_LldpV2Xdot1RemCdcpTlvString_Object=MibTableColumn
lldpV2Xdot1RemCdcpTlvString=_LldpV2Xdot1RemCdcpTlvString_Object((1,3,111,2,802,1,1,13,1,5,32962,7,1,1,1,3,2,1,1),_LldpV2Xdot1RemCdcpTlvString_Type())
lldpV2Xdot1RemCdcpTlvString.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpV2Xdot1RemCdcpTlvString.setStatus(_A)
_LldpXdot1EvbConformance_ObjectIdentity=ObjectIdentity
lldpXdot1EvbConformance=_LldpXdot1EvbConformance_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,2))
_LldpXdot1EvbCompliances_ObjectIdentity=ObjectIdentity
lldpXdot1EvbCompliances=_LldpXdot1EvbCompliances_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,2,1))
_LldpXdot1EvbGroups_ObjectIdentity=ObjectIdentity
lldpXdot1EvbGroups=_LldpXdot1EvbGroups_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,1,2,2))
lldpV2PortConfigEntry.registerAugmentions((_C,_N))
lldpXdot1EvbConfigEvbEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions((_C,_O))
lldpXdot1EvbConfigCdcpEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpXdot1EvbGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,32962,7,1,2,2,1))
lldpXdot1EvbGroup.setObjects(*((_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:lldpXdot1EvbGroup.setStatus(_A)
lldpXdot1EvbCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,32962,7,1,2,1,1))
lldpXdot1EvbCompliance.setObjects(*((_C,_V),(_C,_L)))
if mibBuilder.loadTexts:lldpXdot1EvbCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lldpXdot1StandAloneExtensions':lldpXdot1StandAloneExtensions,'lldpXDot1EvbExtensions':lldpXDot1EvbExtensions,'lldpXdot1EvbMIB':lldpXdot1EvbMIB,'lldpXdot1EvbObjects':lldpXdot1EvbObjects,'lldpXdot1EvbConfig':lldpXdot1EvbConfig,'lldpXdot1EvbConfigEvbTable':lldpXdot1EvbConfigEvbTable,_N:lldpXdot1EvbConfigEvbEntry,_P:lldpXdot1EvbConfigEvbTxEnable,'lldpXdot1EvbConfigCdcpTable':lldpXdot1EvbConfigCdcpTable,_O:lldpXdot1EvbConfigCdcpEntry,_Q:lldpXdot1EvbConfigCdcpTxEnable,'lldpXdot1EvbLocalData':lldpXdot1EvbLocalData,'lldpV2Xdot1LocEvbTlvTable':lldpV2Xdot1LocEvbTlvTable,'lldpV2Xdot1LocEvbTlvEntry':lldpV2Xdot1LocEvbTlvEntry,_R:lldpV2Xdot1LocEvbTlvString,'lldpV2Xdot1LocCdcpTlvTable':lldpV2Xdot1LocCdcpTlvTable,'lldpV2Xdot1LocCdcpTlvEntry':lldpV2Xdot1LocCdcpTlvEntry,_S:lldpV2Xdot1LocCdcpTlvString,'lldpXdot1EvbRemoteData':lldpXdot1EvbRemoteData,'lldpV2Xdot1RemEvbTlvTable':lldpV2Xdot1RemEvbTlvTable,'lldpV2Xdot1RemEvbTlvEntry':lldpV2Xdot1RemEvbTlvEntry,_T:lldpV2Xdot1RemEvbTlvString,'lldpV2Xdot1RemCdcpTlvTable':lldpV2Xdot1RemCdcpTlvTable,'lldpV2Xdot1RemCdcpTlvEntry':lldpV2Xdot1RemCdcpTlvEntry,_U:lldpV2Xdot1RemCdcpTlvString,'lldpXdot1EvbConformance':lldpXdot1EvbConformance,'lldpXdot1EvbCompliances':lldpXdot1EvbCompliances,'lldpXdot1EvbCompliance':lldpXdot1EvbCompliance,'lldpXdot1EvbGroups':lldpXdot1EvbGroups,_V:lldpXdot1EvbGroup})