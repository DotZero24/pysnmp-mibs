_h='fsUrpfMIBVrfObjectGroup'
_g='fsUrpfMIBNotifyGroup'
_f='fsUrpfMIBMainObjectGroup'
_e='fsUrpfIfDropRateNotify'
_d='fsUrpfIfVrfName'
_c='fsUrpfIfWhichRouteTableID'
_b='fsUrpfIfNotifyDrHoldDownReset'
_a='fsUrpfIfNotifyDropRateThreshold'
_Z='fsUrpfIfDropRateNotifyEnable'
_Y='fsUrpfIfCheckStrict'
_X='fsUrpfIfDrops'
_W='fsUrpfDropRate'
_V='fsUrpfDrops'
_U='fsUrpfDropNotifyHoldDownTime'
_T='fsUrpfDropRateWindow'
_S='fsUrpfComputeInterval'
_R='fsUrpfIfConfEntry'
_Q='packets/second'
_P='fsUrpfIfIpVersion'
_O='packets'
_N='not-accessible'
_M='fsUrpfIpVersion'
_L='Unsigned32'
_K='SnmpAdminString'
_J='ifIndex'
_I='IF-MIB'
_H='fsUrpfIfDropRate'
_G='seconds'
_F='TruthValue'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='FS-URPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ifIndex,=mibBuilder.importSymbols(_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
fsUrpfMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,46))
if mibBuilder.loadTexts:fsUrpfMIB.setRevisions(('2009-04-09 00:00',))
_FsUrpfMIBObjects_ObjectIdentity=ObjectIdentity
fsUrpfMIBObjects=_FsUrpfMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,0))
_FsUrpfScalar_ObjectIdentity=ObjectIdentity
fsUrpfScalar=_FsUrpfScalar_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,0,1))
class _FsUrpfComputeInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_FsUrpfComputeInterval_Type.__name__=_C
_FsUrpfComputeInterval_Object=MibScalar
fsUrpfComputeInterval=_FsUrpfComputeInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,1,1),_FsUrpfComputeInterval_Type())
fsUrpfComputeInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsUrpfComputeInterval.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfComputeInterval.setUnits(_G)
class _FsUrpfDropRateWindow_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,1500))
_FsUrpfDropRateWindow_Type.__name__=_C
_FsUrpfDropRateWindow_Object=MibScalar
fsUrpfDropRateWindow=_FsUrpfDropRateWindow_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,1,2),_FsUrpfDropRateWindow_Type())
fsUrpfDropRateWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfDropRateWindow.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfDropRateWindow.setUnits(_G)
class _FsUrpfDropNotifyHoldDownTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_FsUrpfDropNotifyHoldDownTime_Type.__name__=_C
_FsUrpfDropNotifyHoldDownTime_Object=MibScalar
fsUrpfDropNotifyHoldDownTime=_FsUrpfDropNotifyHoldDownTime_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,1,3),_FsUrpfDropNotifyHoldDownTime_Type())
fsUrpfDropNotifyHoldDownTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsUrpfDropNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfDropNotifyHoldDownTime.setUnits(_G)
_FsUrpfStatistics_ObjectIdentity=ObjectIdentity
fsUrpfStatistics=_FsUrpfStatistics_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,0,2))
_FsUrpfTable_Object=MibTable
fsUrpfTable=_FsUrpfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,1))
if mibBuilder.loadTexts:fsUrpfTable.setStatus(_A)
_FsUrpfEntry_Object=MibTableRow
fsUrpfEntry=_FsUrpfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,1,1))
fsUrpfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:fsUrpfEntry.setStatus(_A)
class _FsUrpfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_FsUrpfIpVersion_Type.__name__=_C
_FsUrpfIpVersion_Object=MibTableColumn
fsUrpfIpVersion=_FsUrpfIpVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,1,1,1),_FsUrpfIpVersion_Type())
fsUrpfIpVersion.setMaxAccess(_N)
if mibBuilder.loadTexts:fsUrpfIpVersion.setStatus(_A)
_FsUrpfDrops_Type=Counter32
_FsUrpfDrops_Object=MibTableColumn
fsUrpfDrops=_FsUrpfDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,1,1,2),_FsUrpfDrops_Type())
fsUrpfDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfDrops.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfDrops.setUnits(_O)
_FsUrpfDropRate_Type=Gauge32
_FsUrpfDropRate_Object=MibTableColumn
fsUrpfDropRate=_FsUrpfDropRate_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,1,1,3),_FsUrpfDropRate_Type())
fsUrpfDropRate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfDropRate.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfDropRate.setUnits('packets per second')
_FsUrpfIfMonTable_Object=MibTable
fsUrpfIfMonTable=_FsUrpfIfMonTable_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,2))
if mibBuilder.loadTexts:fsUrpfIfMonTable.setStatus(_A)
_FsUrpfIfMonEntry_Object=MibTableRow
fsUrpfIfMonEntry=_FsUrpfIfMonEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,2,1))
fsUrpfIfMonEntry.setIndexNames((0,_I,_J),(0,_B,_P))
if mibBuilder.loadTexts:fsUrpfIfMonEntry.setStatus(_A)
class _FsUrpfIfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_FsUrpfIfIpVersion_Type.__name__=_C
_FsUrpfIfIpVersion_Object=MibTableColumn
fsUrpfIfIpVersion=_FsUrpfIfIpVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,2,1,1),_FsUrpfIfIpVersion_Type())
fsUrpfIfIpVersion.setMaxAccess(_N)
if mibBuilder.loadTexts:fsUrpfIfIpVersion.setStatus(_A)
_FsUrpfIfDrops_Type=Counter32
_FsUrpfIfDrops_Object=MibTableColumn
fsUrpfIfDrops=_FsUrpfIfDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,2,1,2),_FsUrpfIfDrops_Type())
fsUrpfIfDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfIfDrops.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfIfDrops.setUnits(_O)
_FsUrpfIfDropRate_Type=Gauge32
_FsUrpfIfDropRate_Object=MibTableColumn
fsUrpfIfDropRate=_FsUrpfIfDropRate_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,2,2,1,3),_FsUrpfIfDropRate_Type())
fsUrpfIfDropRate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfIfDropRate.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfIfDropRate.setUnits(_Q)
_FsUrpfInterfaceConfig_ObjectIdentity=ObjectIdentity
fsUrpfInterfaceConfig=_FsUrpfInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,0,3))
_FsUrpfIfConfTable_Object=MibTable
fsUrpfIfConfTable=_FsUrpfIfConfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1))
if mibBuilder.loadTexts:fsUrpfIfConfTable.setStatus(_A)
_FsUrpfIfConfEntry_Object=MibTableRow
fsUrpfIfConfEntry=_FsUrpfIfConfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1))
if mibBuilder.loadTexts:fsUrpfIfConfEntry.setStatus(_A)
class _FsUrpfIfCheckStrict_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('strict',1),('loose',2)))
_FsUrpfIfCheckStrict_Type.__name__=_C
_FsUrpfIfCheckStrict_Object=MibTableColumn
fsUrpfIfCheckStrict=_FsUrpfIfCheckStrict_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,1),_FsUrpfIfCheckStrict_Type())
fsUrpfIfCheckStrict.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfIfCheckStrict.setStatus(_A)
class _FsUrpfIfDropRateNotifyEnable_Type(TruthValue):defaultValue=2
_FsUrpfIfDropRateNotifyEnable_Type.__name__=_F
_FsUrpfIfDropRateNotifyEnable_Object=MibTableColumn
fsUrpfIfDropRateNotifyEnable=_FsUrpfIfDropRateNotifyEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,2),_FsUrpfIfDropRateNotifyEnable_Type())
fsUrpfIfDropRateNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsUrpfIfDropRateNotifyEnable.setStatus(_A)
class _FsUrpfIfNotifyDropRateThreshold_Type(Unsigned32):defaultValue=1000
_FsUrpfIfNotifyDropRateThreshold_Type.__name__=_L
_FsUrpfIfNotifyDropRateThreshold_Object=MibTableColumn
fsUrpfIfNotifyDropRateThreshold=_FsUrpfIfNotifyDropRateThreshold_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,3),_FsUrpfIfNotifyDropRateThreshold_Type())
fsUrpfIfNotifyDropRateThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:fsUrpfIfNotifyDropRateThreshold.setStatus(_A)
if mibBuilder.loadTexts:fsUrpfIfNotifyDropRateThreshold.setUnits(_Q)
class _FsUrpfIfNotifyDrHoldDownReset_Type(TruthValue):defaultValue=2
_FsUrpfIfNotifyDrHoldDownReset_Type.__name__=_F
_FsUrpfIfNotifyDrHoldDownReset_Object=MibTableColumn
fsUrpfIfNotifyDrHoldDownReset=_FsUrpfIfNotifyDrHoldDownReset_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,4),_FsUrpfIfNotifyDrHoldDownReset_Type())
fsUrpfIfNotifyDrHoldDownReset.setMaxAccess(_E)
if mibBuilder.loadTexts:fsUrpfIfNotifyDrHoldDownReset.setStatus(_A)
class _FsUrpfIfWhichRouteTableID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('vrf',2)))
_FsUrpfIfWhichRouteTableID_Type.__name__=_C
_FsUrpfIfWhichRouteTableID_Object=MibTableColumn
fsUrpfIfWhichRouteTableID=_FsUrpfIfWhichRouteTableID_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,5),_FsUrpfIfWhichRouteTableID_Type())
fsUrpfIfWhichRouteTableID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfIfWhichRouteTableID.setStatus(_A)
class _FsUrpfIfVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsUrpfIfVrfName_Type.__name__=_K
_FsUrpfIfVrfName_Object=MibTableColumn
fsUrpfIfVrfName=_FsUrpfIfVrfName_Object((1,3,6,1,4,1,52642,1,1,10,2,46,0,3,1,1,6),_FsUrpfIfVrfName_Type())
fsUrpfIfVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsUrpfIfVrfName.setStatus(_A)
_FsUrpfMIBNotifs_ObjectIdentity=ObjectIdentity
fsUrpfMIBNotifs=_FsUrpfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,1))
_FsUrpfMIBConformance_ObjectIdentity=ObjectIdentity
fsUrpfMIBConformance=_FsUrpfMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,2))
_FsUrpfMIBCompliances_ObjectIdentity=ObjectIdentity
fsUrpfMIBCompliances=_FsUrpfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,2,1))
_FsUrpfMIBGroups_ObjectIdentity=ObjectIdentity
fsUrpfMIBGroups=_FsUrpfMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,46,2,2))
fsUrpfIfMonEntry.registerAugmentions((_B,_R))
fsUrpfIfConfEntry.setIndexNames(*fsUrpfIfMonEntry.getIndexNames())
fsUrpfMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,46,2,2,1))
fsUrpfMIBMainObjectGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:fsUrpfMIBMainObjectGroup.setStatus(_A)
fsUrpfMIBVrfObjectGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,46,2,2,2))
fsUrpfMIBVrfObjectGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:fsUrpfMIBVrfObjectGroup.setStatus(_A)
fsUrpfIfDropRateNotify=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,46,1,1))
fsUrpfIfDropRateNotify.setObjects((_B,_H))
if mibBuilder.loadTexts:fsUrpfIfDropRateNotify.setStatus(_A)
fsUrpfMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,46,2,2,3))
fsUrpfMIBNotifyGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:fsUrpfMIBNotifyGroup.setStatus(_A)
fsUrpfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,46,2,1,1))
fsUrpfMIBCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:fsUrpfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsUrpfMIB':fsUrpfMIB,'fsUrpfMIBObjects':fsUrpfMIBObjects,'fsUrpfScalar':fsUrpfScalar,_S:fsUrpfComputeInterval,_T:fsUrpfDropRateWindow,_U:fsUrpfDropNotifyHoldDownTime,'fsUrpfStatistics':fsUrpfStatistics,'fsUrpfTable':fsUrpfTable,'fsUrpfEntry':fsUrpfEntry,_M:fsUrpfIpVersion,_V:fsUrpfDrops,_W:fsUrpfDropRate,'fsUrpfIfMonTable':fsUrpfIfMonTable,'fsUrpfIfMonEntry':fsUrpfIfMonEntry,_P:fsUrpfIfIpVersion,_X:fsUrpfIfDrops,_H:fsUrpfIfDropRate,'fsUrpfInterfaceConfig':fsUrpfInterfaceConfig,'fsUrpfIfConfTable':fsUrpfIfConfTable,_R:fsUrpfIfConfEntry,_Y:fsUrpfIfCheckStrict,_Z:fsUrpfIfDropRateNotifyEnable,_a:fsUrpfIfNotifyDropRateThreshold,_b:fsUrpfIfNotifyDrHoldDownReset,_c:fsUrpfIfWhichRouteTableID,_d:fsUrpfIfVrfName,'fsUrpfMIBNotifs':fsUrpfMIBNotifs,_e:fsUrpfIfDropRateNotify,'fsUrpfMIBConformance':fsUrpfMIBConformance,'fsUrpfMIBCompliances':fsUrpfMIBCompliances,'fsUrpfMIBCompliance':fsUrpfMIBCompliance,'fsUrpfMIBGroups':fsUrpfMIBGroups,_f:fsUrpfMIBMainObjectGroup,_h:fsUrpfMIBVrfObjectGroup,_g:fsUrpfMIBNotifyGroup})