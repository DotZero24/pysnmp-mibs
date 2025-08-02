_h='qtechUrpfMIBVrfObjectGroup'
_g='qtechUrpfMIBNotifyGroup'
_f='qtechUrpfMIBMainObjectGroup'
_e='qtechUrpfIfDropRateNotify'
_d='qtechUrpfIfVrfName'
_c='qtechUrpfIfWhichRouteTableID'
_b='qtechUrpfIfNotifyDrHoldDownReset'
_a='qtechUrpfIfNotifyDropRateThreshold'
_Z='qtechUrpfIfDropRateNotifyEnable'
_Y='qtechUrpfIfCheckStrict'
_X='qtechUrpfIfDrops'
_W='qtechUrpfDropRate'
_V='qtechUrpfDrops'
_U='qtechUrpfDropNotifyHoldDownTime'
_T='qtechUrpfDropRateWindow'
_S='qtechUrpfComputeInterval'
_R='qtechUrpfIfConfEntry'
_Q='packets/second'
_P='qtechUrpfIfIpVersion'
_O='packets'
_N='not-accessible'
_M='qtechUrpfIpVersion'
_L='Unsigned32'
_K='SnmpAdminString'
_J='ifIndex'
_I='IF-MIB'
_H='qtechUrpfIfDropRate'
_G='seconds'
_F='TruthValue'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='QTECH-URPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
qtechUrpfMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,46))
if mibBuilder.loadTexts:qtechUrpfMIB.setRevisions(('2009-04-09 00:00',))
_QtechUrpfMIBObjects_ObjectIdentity=ObjectIdentity
qtechUrpfMIBObjects=_QtechUrpfMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,0))
_QtechUrpfScalar_ObjectIdentity=ObjectIdentity
qtechUrpfScalar=_QtechUrpfScalar_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,0,1))
class _QtechUrpfComputeInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_QtechUrpfComputeInterval_Type.__name__=_C
_QtechUrpfComputeInterval_Object=MibScalar
qtechUrpfComputeInterval=_QtechUrpfComputeInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,1,1),_QtechUrpfComputeInterval_Type())
qtechUrpfComputeInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechUrpfComputeInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfComputeInterval.setUnits(_G)
class _QtechUrpfDropRateWindow_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,1500))
_QtechUrpfDropRateWindow_Type.__name__=_C
_QtechUrpfDropRateWindow_Object=MibScalar
qtechUrpfDropRateWindow=_QtechUrpfDropRateWindow_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,1,2),_QtechUrpfDropRateWindow_Type())
qtechUrpfDropRateWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfDropRateWindow.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfDropRateWindow.setUnits(_G)
class _QtechUrpfDropNotifyHoldDownTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_QtechUrpfDropNotifyHoldDownTime_Type.__name__=_C
_QtechUrpfDropNotifyHoldDownTime_Object=MibScalar
qtechUrpfDropNotifyHoldDownTime=_QtechUrpfDropNotifyHoldDownTime_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,1,3),_QtechUrpfDropNotifyHoldDownTime_Type())
qtechUrpfDropNotifyHoldDownTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechUrpfDropNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfDropNotifyHoldDownTime.setUnits(_G)
_QtechUrpfStatistics_ObjectIdentity=ObjectIdentity
qtechUrpfStatistics=_QtechUrpfStatistics_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,0,2))
_QtechUrpfTable_Object=MibTable
qtechUrpfTable=_QtechUrpfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,1))
if mibBuilder.loadTexts:qtechUrpfTable.setStatus(_A)
_QtechUrpfEntry_Object=MibTableRow
qtechUrpfEntry=_QtechUrpfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,1,1))
qtechUrpfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechUrpfEntry.setStatus(_A)
class _QtechUrpfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_QtechUrpfIpVersion_Type.__name__=_C
_QtechUrpfIpVersion_Object=MibTableColumn
qtechUrpfIpVersion=_QtechUrpfIpVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,1,1,1),_QtechUrpfIpVersion_Type())
qtechUrpfIpVersion.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechUrpfIpVersion.setStatus(_A)
_QtechUrpfDrops_Type=Counter32
_QtechUrpfDrops_Object=MibTableColumn
qtechUrpfDrops=_QtechUrpfDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,1,1,2),_QtechUrpfDrops_Type())
qtechUrpfDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfDrops.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfDrops.setUnits(_O)
_QtechUrpfDropRate_Type=Gauge32
_QtechUrpfDropRate_Object=MibTableColumn
qtechUrpfDropRate=_QtechUrpfDropRate_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,1,1,3),_QtechUrpfDropRate_Type())
qtechUrpfDropRate.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfDropRate.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfDropRate.setUnits('packets per second')
_QtechUrpfIfMonTable_Object=MibTable
qtechUrpfIfMonTable=_QtechUrpfIfMonTable_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,2))
if mibBuilder.loadTexts:qtechUrpfIfMonTable.setStatus(_A)
_QtechUrpfIfMonEntry_Object=MibTableRow
qtechUrpfIfMonEntry=_QtechUrpfIfMonEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,2,1))
qtechUrpfIfMonEntry.setIndexNames((0,_I,_J),(0,_B,_P))
if mibBuilder.loadTexts:qtechUrpfIfMonEntry.setStatus(_A)
class _QtechUrpfIfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_QtechUrpfIfIpVersion_Type.__name__=_C
_QtechUrpfIfIpVersion_Object=MibTableColumn
qtechUrpfIfIpVersion=_QtechUrpfIfIpVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,2,1,1),_QtechUrpfIfIpVersion_Type())
qtechUrpfIfIpVersion.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechUrpfIfIpVersion.setStatus(_A)
_QtechUrpfIfDrops_Type=Counter32
_QtechUrpfIfDrops_Object=MibTableColumn
qtechUrpfIfDrops=_QtechUrpfIfDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,2,1,2),_QtechUrpfIfDrops_Type())
qtechUrpfIfDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfIfDrops.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfIfDrops.setUnits(_O)
_QtechUrpfIfDropRate_Type=Gauge32
_QtechUrpfIfDropRate_Object=MibTableColumn
qtechUrpfIfDropRate=_QtechUrpfIfDropRate_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,2,2,1,3),_QtechUrpfIfDropRate_Type())
qtechUrpfIfDropRate.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfIfDropRate.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfIfDropRate.setUnits(_Q)
_QtechUrpfInterfaceConfig_ObjectIdentity=ObjectIdentity
qtechUrpfInterfaceConfig=_QtechUrpfInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,0,3))
_QtechUrpfIfConfTable_Object=MibTable
qtechUrpfIfConfTable=_QtechUrpfIfConfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1))
if mibBuilder.loadTexts:qtechUrpfIfConfTable.setStatus(_A)
_QtechUrpfIfConfEntry_Object=MibTableRow
qtechUrpfIfConfEntry=_QtechUrpfIfConfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1))
if mibBuilder.loadTexts:qtechUrpfIfConfEntry.setStatus(_A)
class _QtechUrpfIfCheckStrict_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('strict',1),('loose',2)))
_QtechUrpfIfCheckStrict_Type.__name__=_C
_QtechUrpfIfCheckStrict_Object=MibTableColumn
qtechUrpfIfCheckStrict=_QtechUrpfIfCheckStrict_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,1),_QtechUrpfIfCheckStrict_Type())
qtechUrpfIfCheckStrict.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfIfCheckStrict.setStatus(_A)
class _QtechUrpfIfDropRateNotifyEnable_Type(TruthValue):defaultValue=2
_QtechUrpfIfDropRateNotifyEnable_Type.__name__=_F
_QtechUrpfIfDropRateNotifyEnable_Object=MibTableColumn
qtechUrpfIfDropRateNotifyEnable=_QtechUrpfIfDropRateNotifyEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,2),_QtechUrpfIfDropRateNotifyEnable_Type())
qtechUrpfIfDropRateNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechUrpfIfDropRateNotifyEnable.setStatus(_A)
class _QtechUrpfIfNotifyDropRateThreshold_Type(Unsigned32):defaultValue=1000
_QtechUrpfIfNotifyDropRateThreshold_Type.__name__=_L
_QtechUrpfIfNotifyDropRateThreshold_Object=MibTableColumn
qtechUrpfIfNotifyDropRateThreshold=_QtechUrpfIfNotifyDropRateThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,3),_QtechUrpfIfNotifyDropRateThreshold_Type())
qtechUrpfIfNotifyDropRateThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechUrpfIfNotifyDropRateThreshold.setStatus(_A)
if mibBuilder.loadTexts:qtechUrpfIfNotifyDropRateThreshold.setUnits(_Q)
class _QtechUrpfIfNotifyDrHoldDownReset_Type(TruthValue):defaultValue=2
_QtechUrpfIfNotifyDrHoldDownReset_Type.__name__=_F
_QtechUrpfIfNotifyDrHoldDownReset_Object=MibTableColumn
qtechUrpfIfNotifyDrHoldDownReset=_QtechUrpfIfNotifyDrHoldDownReset_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,4),_QtechUrpfIfNotifyDrHoldDownReset_Type())
qtechUrpfIfNotifyDrHoldDownReset.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechUrpfIfNotifyDrHoldDownReset.setStatus(_A)
class _QtechUrpfIfWhichRouteTableID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('vrf',2)))
_QtechUrpfIfWhichRouteTableID_Type.__name__=_C
_QtechUrpfIfWhichRouteTableID_Object=MibTableColumn
qtechUrpfIfWhichRouteTableID=_QtechUrpfIfWhichRouteTableID_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,5),_QtechUrpfIfWhichRouteTableID_Type())
qtechUrpfIfWhichRouteTableID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfIfWhichRouteTableID.setStatus(_A)
class _QtechUrpfIfVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechUrpfIfVrfName_Type.__name__=_K
_QtechUrpfIfVrfName_Object=MibTableColumn
qtechUrpfIfVrfName=_QtechUrpfIfVrfName_Object((1,3,6,1,4,1,27514,1,1,10,2,46,0,3,1,1,6),_QtechUrpfIfVrfName_Type())
qtechUrpfIfVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechUrpfIfVrfName.setStatus(_A)
_QtechUrpfMIBNotifs_ObjectIdentity=ObjectIdentity
qtechUrpfMIBNotifs=_QtechUrpfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,1))
_QtechUrpfMIBConformance_ObjectIdentity=ObjectIdentity
qtechUrpfMIBConformance=_QtechUrpfMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,2))
_QtechUrpfMIBCompliances_ObjectIdentity=ObjectIdentity
qtechUrpfMIBCompliances=_QtechUrpfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,2,1))
_QtechUrpfMIBGroups_ObjectIdentity=ObjectIdentity
qtechUrpfMIBGroups=_QtechUrpfMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,46,2,2))
qtechUrpfIfMonEntry.registerAugmentions((_B,_R))
qtechUrpfIfConfEntry.setIndexNames(*qtechUrpfIfMonEntry.getIndexNames())
qtechUrpfMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,46,2,2,1))
qtechUrpfMIBMainObjectGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_H),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:qtechUrpfMIBMainObjectGroup.setStatus(_A)
qtechUrpfMIBVrfObjectGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,46,2,2,2))
qtechUrpfMIBVrfObjectGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:qtechUrpfMIBVrfObjectGroup.setStatus(_A)
qtechUrpfIfDropRateNotify=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,46,1,1))
qtechUrpfIfDropRateNotify.setObjects((_B,_H))
if mibBuilder.loadTexts:qtechUrpfIfDropRateNotify.setStatus(_A)
qtechUrpfMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,46,2,2,3))
qtechUrpfMIBNotifyGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:qtechUrpfMIBNotifyGroup.setStatus(_A)
qtechUrpfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,46,2,1,1))
qtechUrpfMIBCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:qtechUrpfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechUrpfMIB':qtechUrpfMIB,'qtechUrpfMIBObjects':qtechUrpfMIBObjects,'qtechUrpfScalar':qtechUrpfScalar,_S:qtechUrpfComputeInterval,_T:qtechUrpfDropRateWindow,_U:qtechUrpfDropNotifyHoldDownTime,'qtechUrpfStatistics':qtechUrpfStatistics,'qtechUrpfTable':qtechUrpfTable,'qtechUrpfEntry':qtechUrpfEntry,_M:qtechUrpfIpVersion,_V:qtechUrpfDrops,_W:qtechUrpfDropRate,'qtechUrpfIfMonTable':qtechUrpfIfMonTable,'qtechUrpfIfMonEntry':qtechUrpfIfMonEntry,_P:qtechUrpfIfIpVersion,_X:qtechUrpfIfDrops,_H:qtechUrpfIfDropRate,'qtechUrpfInterfaceConfig':qtechUrpfInterfaceConfig,'qtechUrpfIfConfTable':qtechUrpfIfConfTable,_R:qtechUrpfIfConfEntry,_Y:qtechUrpfIfCheckStrict,_Z:qtechUrpfIfDropRateNotifyEnable,_a:qtechUrpfIfNotifyDropRateThreshold,_b:qtechUrpfIfNotifyDrHoldDownReset,_c:qtechUrpfIfWhichRouteTableID,_d:qtechUrpfIfVrfName,'qtechUrpfMIBNotifs':qtechUrpfMIBNotifs,_e:qtechUrpfIfDropRateNotify,'qtechUrpfMIBConformance':qtechUrpfMIBConformance,'qtechUrpfMIBCompliances':qtechUrpfMIBCompliances,'qtechUrpfMIBCompliance':qtechUrpfMIBCompliance,'qtechUrpfMIBGroups':qtechUrpfMIBGroups,_f:qtechUrpfMIBMainObjectGroup,_h:qtechUrpfMIBVrfObjectGroup,_g:qtechUrpfMIBNotifyGroup})