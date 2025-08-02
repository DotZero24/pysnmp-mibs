_n='ciscoIpUrpfMIBVrfObjectGroup'
_m='ciscoIpUrpfMIBNotifyGroup'
_l='ciscoIpUrpfMIBMainObjectGroup'
_k='cipUrpfIfDropRateNotify'
_j='cipUrpfVrfIfDiscontinuityTime'
_i='cipUrpfVrfIfDrops'
_h='cipUrpfIfVrfName'
_g='cipUrpfIfWhichRouteTableID'
_f='cipUrpfIfDiscontinuityTime'
_e='cipUrpfIfCheckStrict'
_d='cipUrpfIfNotifyDrHoldDownReset'
_c='cipUrpfIfNotifyDropRateThreshold'
_b='cipUrpfIfDropRateNotifyEnable'
_a='cipUrpfIfSuppressedDrops'
_Z='cipUrpfIfDrops'
_Y='cipUrpfDropRate'
_X='cipUrpfDrops'
_W='cipUrpfDropNotifyHoldDownTime'
_V='cipUrpfComputeInterval'
_U='cipUrpfDropRateWindow'
_T='cipUrpfIfConfEntry'
_S='packets/second'
_R='cipUrpfIfIpVersion'
_Q='not-accessible'
_P='cipUrpfIpVersion'
_O='strict'
_N='Unsigned32'
_M='cipUrpfIfDropRate'
_L='seconds'
_K='TruthValue'
_J='SnmpAdminString'
_I='ifIndex'
_H='IF-MIB'
_G='cipUrpfVrfName'
_F='packets'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-IP-URPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_K)
ciscoIpUrpfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,451))
if mibBuilder.loadTexts:ciscoIpUrpfMIB.setRevisions(('2011-12-29 00:00','2004-11-12 00:00'))
class UnicastRpfType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('loose',2),('disabled',3)))
class UnicastRpfOptions(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('allowDefault',0),('allowSelfPing',1)))
_CiscoIpUrpfMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpUrpfMIBNotifs=_CiscoIpUrpfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,451,0))
_CiscoIpUrpfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpUrpfMIBObjects=_CiscoIpUrpfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,451,1))
_CipUrpfScalar_ObjectIdentity=ObjectIdentity
cipUrpfScalar=_CipUrpfScalar_ObjectIdentity((1,3,6,1,4,1,9,9,451,1,1))
class _CipUrpfDropRateWindow_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CipUrpfDropRateWindow_Type.__name__=_D
_CipUrpfDropRateWindow_Object=MibScalar
cipUrpfDropRateWindow=_CipUrpfDropRateWindow_Object((1,3,6,1,4,1,9,9,451,1,1,1),_CipUrpfDropRateWindow_Type())
cipUrpfDropRateWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfDropRateWindow.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfDropRateWindow.setUnits(_L)
class _CipUrpfComputeInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CipUrpfComputeInterval_Type.__name__=_D
_CipUrpfComputeInterval_Object=MibScalar
cipUrpfComputeInterval=_CipUrpfComputeInterval_Object((1,3,6,1,4,1,9,9,451,1,1,2),_CipUrpfComputeInterval_Type())
cipUrpfComputeInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfComputeInterval.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfComputeInterval.setUnits(_L)
class _CipUrpfDropNotifyHoldDownTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CipUrpfDropNotifyHoldDownTime_Type.__name__=_D
_CipUrpfDropNotifyHoldDownTime_Object=MibScalar
cipUrpfDropNotifyHoldDownTime=_CipUrpfDropNotifyHoldDownTime_Object((1,3,6,1,4,1,9,9,451,1,1,3),_CipUrpfDropNotifyHoldDownTime_Type())
cipUrpfDropNotifyHoldDownTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfDropNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfDropNotifyHoldDownTime.setUnits(_L)
_CipUrpfStatistics_ObjectIdentity=ObjectIdentity
cipUrpfStatistics=_CipUrpfStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,451,1,2))
_CipUrpfTable_Object=MibTable
cipUrpfTable=_CipUrpfTable_Object((1,3,6,1,4,1,9,9,451,1,2,1))
if mibBuilder.loadTexts:cipUrpfTable.setStatus(_A)
_CipUrpfEntry_Object=MibTableRow
cipUrpfEntry=_CipUrpfEntry_Object((1,3,6,1,4,1,9,9,451,1,2,1,1))
cipUrpfEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cipUrpfEntry.setStatus(_A)
class _CipUrpfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_CipUrpfIpVersion_Type.__name__=_D
_CipUrpfIpVersion_Object=MibTableColumn
cipUrpfIpVersion=_CipUrpfIpVersion_Object((1,3,6,1,4,1,9,9,451,1,2,1,1,1),_CipUrpfIpVersion_Type())
cipUrpfIpVersion.setMaxAccess(_Q)
if mibBuilder.loadTexts:cipUrpfIpVersion.setStatus(_A)
_CipUrpfDrops_Type=Counter32
_CipUrpfDrops_Object=MibTableColumn
cipUrpfDrops=_CipUrpfDrops_Object((1,3,6,1,4,1,9,9,451,1,2,1,1,2),_CipUrpfDrops_Type())
cipUrpfDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfDrops.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfDrops.setUnits(_F)
_CipUrpfDropRate_Type=Gauge32
_CipUrpfDropRate_Object=MibTableColumn
cipUrpfDropRate=_CipUrpfDropRate_Object((1,3,6,1,4,1,9,9,451,1,2,1,1,3),_CipUrpfDropRate_Type())
cipUrpfDropRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfDropRate.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfDropRate.setUnits('packets per second')
_CipUrpfIfMonTable_Object=MibTable
cipUrpfIfMonTable=_CipUrpfIfMonTable_Object((1,3,6,1,4,1,9,9,451,1,2,2))
if mibBuilder.loadTexts:cipUrpfIfMonTable.setStatus(_A)
_CipUrpfIfMonEntry_Object=MibTableRow
cipUrpfIfMonEntry=_CipUrpfIfMonEntry_Object((1,3,6,1,4,1,9,9,451,1,2,2,1))
cipUrpfIfMonEntry.setIndexNames((0,_H,_I),(0,_B,_R))
if mibBuilder.loadTexts:cipUrpfIfMonEntry.setStatus(_A)
class _CipUrpfIfIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_CipUrpfIfIpVersion_Type.__name__=_D
_CipUrpfIfIpVersion_Object=MibTableColumn
cipUrpfIfIpVersion=_CipUrpfIfIpVersion_Object((1,3,6,1,4,1,9,9,451,1,2,2,1,1),_CipUrpfIfIpVersion_Type())
cipUrpfIfIpVersion.setMaxAccess(_Q)
if mibBuilder.loadTexts:cipUrpfIfIpVersion.setStatus(_A)
_CipUrpfIfDrops_Type=Counter32
_CipUrpfIfDrops_Object=MibTableColumn
cipUrpfIfDrops=_CipUrpfIfDrops_Object((1,3,6,1,4,1,9,9,451,1,2,2,1,2),_CipUrpfIfDrops_Type())
cipUrpfIfDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfDrops.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfIfDrops.setUnits(_F)
_CipUrpfIfSuppressedDrops_Type=Counter32
_CipUrpfIfSuppressedDrops_Object=MibTableColumn
cipUrpfIfSuppressedDrops=_CipUrpfIfSuppressedDrops_Object((1,3,6,1,4,1,9,9,451,1,2,2,1,3),_CipUrpfIfSuppressedDrops_Type())
cipUrpfIfSuppressedDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfSuppressedDrops.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfIfSuppressedDrops.setUnits(_F)
_CipUrpfIfDropRate_Type=Gauge32
_CipUrpfIfDropRate_Object=MibTableColumn
cipUrpfIfDropRate=_CipUrpfIfDropRate_Object((1,3,6,1,4,1,9,9,451,1,2,2,1,4),_CipUrpfIfDropRate_Type())
cipUrpfIfDropRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfDropRate.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfIfDropRate.setUnits(_S)
_CipUrpfIfDiscontinuityTime_Type=TimeStamp
_CipUrpfIfDiscontinuityTime_Object=MibTableColumn
cipUrpfIfDiscontinuityTime=_CipUrpfIfDiscontinuityTime_Object((1,3,6,1,4,1,9,9,451,1,2,2,1,5),_CipUrpfIfDiscontinuityTime_Type())
cipUrpfIfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfDiscontinuityTime.setStatus(_A)
_CipUrpfVrfIfTable_Object=MibTable
cipUrpfVrfIfTable=_CipUrpfVrfIfTable_Object((1,3,6,1,4,1,9,9,451,1,2,3))
if mibBuilder.loadTexts:cipUrpfVrfIfTable.setStatus(_A)
_CipUrpfVrfIfEntry_Object=MibTableRow
cipUrpfVrfIfEntry=_CipUrpfVrfIfEntry_Object((1,3,6,1,4,1,9,9,451,1,2,3,1))
cipUrpfVrfIfEntry.setIndexNames((0,_B,_G),(0,_H,_I))
if mibBuilder.loadTexts:cipUrpfVrfIfEntry.setStatus(_A)
_CipUrpfVrfIfDrops_Type=Counter32
_CipUrpfVrfIfDrops_Object=MibTableColumn
cipUrpfVrfIfDrops=_CipUrpfVrfIfDrops_Object((1,3,6,1,4,1,9,9,451,1,2,3,1,2),_CipUrpfVrfIfDrops_Type())
cipUrpfVrfIfDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfVrfIfDrops.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfVrfIfDrops.setUnits(_F)
_CipUrpfVrfIfDiscontinuityTime_Type=TimeStamp
_CipUrpfVrfIfDiscontinuityTime_Object=MibTableColumn
cipUrpfVrfIfDiscontinuityTime=_CipUrpfVrfIfDiscontinuityTime_Object((1,3,6,1,4,1,9,9,451,1,2,3,1,3),_CipUrpfVrfIfDiscontinuityTime_Type())
cipUrpfVrfIfDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfVrfIfDiscontinuityTime.setStatus(_A)
_CipUrpfInterfaceConfig_ObjectIdentity=ObjectIdentity
cipUrpfInterfaceConfig=_CipUrpfInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,451,1,3))
_CipUrpfIfConfTable_Object=MibTable
cipUrpfIfConfTable=_CipUrpfIfConfTable_Object((1,3,6,1,4,1,9,9,451,1,3,1))
if mibBuilder.loadTexts:cipUrpfIfConfTable.setStatus(_A)
_CipUrpfIfConfEntry_Object=MibTableRow
cipUrpfIfConfEntry=_CipUrpfIfConfEntry_Object((1,3,6,1,4,1,9,9,451,1,3,1,1))
if mibBuilder.loadTexts:cipUrpfIfConfEntry.setStatus(_A)
class _CipUrpfIfDropRateNotifyEnable_Type(TruthValue):defaultValue=2
_CipUrpfIfDropRateNotifyEnable_Type.__name__=_K
_CipUrpfIfDropRateNotifyEnable_Object=MibTableColumn
cipUrpfIfDropRateNotifyEnable=_CipUrpfIfDropRateNotifyEnable_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,1),_CipUrpfIfDropRateNotifyEnable_Type())
cipUrpfIfDropRateNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfIfDropRateNotifyEnable.setStatus(_A)
class _CipUrpfIfNotifyDropRateThreshold_Type(Unsigned32):defaultValue=1000
_CipUrpfIfNotifyDropRateThreshold_Type.__name__=_N
_CipUrpfIfNotifyDropRateThreshold_Object=MibTableColumn
cipUrpfIfNotifyDropRateThreshold=_CipUrpfIfNotifyDropRateThreshold_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,2),_CipUrpfIfNotifyDropRateThreshold_Type())
cipUrpfIfNotifyDropRateThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfIfNotifyDropRateThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipUrpfIfNotifyDropRateThreshold.setUnits(_S)
class _CipUrpfIfNotifyDrHoldDownReset_Type(TruthValue):defaultValue=2
_CipUrpfIfNotifyDrHoldDownReset_Type.__name__=_K
_CipUrpfIfNotifyDrHoldDownReset_Object=MibTableColumn
cipUrpfIfNotifyDrHoldDownReset=_CipUrpfIfNotifyDrHoldDownReset_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,3),_CipUrpfIfNotifyDrHoldDownReset_Type())
cipUrpfIfNotifyDrHoldDownReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cipUrpfIfNotifyDrHoldDownReset.setStatus(_A)
class _CipUrpfIfCheckStrict_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('loose',2)))
_CipUrpfIfCheckStrict_Type.__name__=_D
_CipUrpfIfCheckStrict_Object=MibTableColumn
cipUrpfIfCheckStrict=_CipUrpfIfCheckStrict_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,4),_CipUrpfIfCheckStrict_Type())
cipUrpfIfCheckStrict.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfCheckStrict.setStatus(_A)
class _CipUrpfIfWhichRouteTableID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('vrf',2)))
_CipUrpfIfWhichRouteTableID_Type.__name__=_D
_CipUrpfIfWhichRouteTableID_Object=MibTableColumn
cipUrpfIfWhichRouteTableID=_CipUrpfIfWhichRouteTableID_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,5),_CipUrpfIfWhichRouteTableID_Type())
cipUrpfIfWhichRouteTableID.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfWhichRouteTableID.setStatus(_A)
class _CipUrpfIfVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipUrpfIfVrfName_Type.__name__=_J
_CipUrpfIfVrfName_Object=MibTableColumn
cipUrpfIfVrfName=_CipUrpfIfVrfName_Object((1,3,6,1,4,1,9,9,451,1,3,1,1,6),_CipUrpfIfVrfName_Type())
cipUrpfIfVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfIfVrfName.setStatus(_A)
_CipUrpfVrf_ObjectIdentity=ObjectIdentity
cipUrpfVrf=_CipUrpfVrf_ObjectIdentity((1,3,6,1,4,1,9,9,451,1,4))
_CipUrpfVrfTable_Object=MibTable
cipUrpfVrfTable=_CipUrpfVrfTable_Object((1,3,6,1,4,1,9,9,451,1,4,1))
if mibBuilder.loadTexts:cipUrpfVrfTable.setStatus(_A)
_CipUrpfVrfEntry_Object=MibTableRow
cipUrpfVrfEntry=_CipUrpfVrfEntry_Object((1,3,6,1,4,1,9,9,451,1,4,1,1))
cipUrpfVrfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cipUrpfVrfEntry.setStatus(_A)
class _CipUrpfVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipUrpfVrfName_Type.__name__=_J
_CipUrpfVrfName_Object=MibTableColumn
cipUrpfVrfName=_CipUrpfVrfName_Object((1,3,6,1,4,1,9,9,451,1,4,1,1,1),_CipUrpfVrfName_Type())
cipUrpfVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipUrpfVrfName.setStatus(_A)
_CiscoIpUrpfMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpUrpfMIBConformance=_CiscoIpUrpfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,451,2))
_CiscoIpUrpfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpUrpfMIBCompliances=_CiscoIpUrpfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,451,2,1))
_CiscoIpUrpfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpUrpfMIBGroups=_CiscoIpUrpfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,451,2,2))
cipUrpfIfMonEntry.registerAugmentions((_B,_T))
cipUrpfIfConfEntry.setIndexNames(*cipUrpfIfMonEntry.getIndexNames())
ciscoIpUrpfMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,451,2,2,1))
ciscoIpUrpfMIBMainObjectGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_M),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoIpUrpfMIBMainObjectGroup.setStatus(_A)
ciscoIpUrpfMIBVrfObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,451,2,2,2))
ciscoIpUrpfMIBVrfObjectGroup.setObjects(*((_B,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoIpUrpfMIBVrfObjectGroup.setStatus(_A)
cipUrpfIfDropRateNotify=NotificationType((1,3,6,1,4,1,9,9,451,0,1))
cipUrpfIfDropRateNotify.setObjects((_B,_M))
if mibBuilder.loadTexts:cipUrpfIfDropRateNotify.setStatus(_A)
ciscoIpUrpfMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,451,2,2,6))
ciscoIpUrpfMIBNotifyGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:ciscoIpUrpfMIBNotifyGroup.setStatus(_A)
ciscoIpUrpfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,451,2,1,1))
ciscoIpUrpfMIBCompliance.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoIpUrpfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'UnicastRpfType':UnicastRpfType,'UnicastRpfOptions':UnicastRpfOptions,'ciscoIpUrpfMIB':ciscoIpUrpfMIB,'ciscoIpUrpfMIBNotifs':ciscoIpUrpfMIBNotifs,_k:cipUrpfIfDropRateNotify,'ciscoIpUrpfMIBObjects':ciscoIpUrpfMIBObjects,'cipUrpfScalar':cipUrpfScalar,_U:cipUrpfDropRateWindow,_V:cipUrpfComputeInterval,_W:cipUrpfDropNotifyHoldDownTime,'cipUrpfStatistics':cipUrpfStatistics,'cipUrpfTable':cipUrpfTable,'cipUrpfEntry':cipUrpfEntry,_P:cipUrpfIpVersion,_X:cipUrpfDrops,_Y:cipUrpfDropRate,'cipUrpfIfMonTable':cipUrpfIfMonTable,'cipUrpfIfMonEntry':cipUrpfIfMonEntry,_R:cipUrpfIfIpVersion,_Z:cipUrpfIfDrops,_a:cipUrpfIfSuppressedDrops,_M:cipUrpfIfDropRate,_f:cipUrpfIfDiscontinuityTime,'cipUrpfVrfIfTable':cipUrpfVrfIfTable,'cipUrpfVrfIfEntry':cipUrpfVrfIfEntry,_i:cipUrpfVrfIfDrops,_j:cipUrpfVrfIfDiscontinuityTime,'cipUrpfInterfaceConfig':cipUrpfInterfaceConfig,'cipUrpfIfConfTable':cipUrpfIfConfTable,_T:cipUrpfIfConfEntry,_b:cipUrpfIfDropRateNotifyEnable,_c:cipUrpfIfNotifyDropRateThreshold,_d:cipUrpfIfNotifyDrHoldDownReset,_e:cipUrpfIfCheckStrict,_g:cipUrpfIfWhichRouteTableID,_h:cipUrpfIfVrfName,'cipUrpfVrf':cipUrpfVrf,'cipUrpfVrfTable':cipUrpfVrfTable,'cipUrpfVrfEntry':cipUrpfVrfEntry,_G:cipUrpfVrfName,'ciscoIpUrpfMIBConformance':ciscoIpUrpfMIBConformance,'ciscoIpUrpfMIBCompliances':ciscoIpUrpfMIBCompliances,'ciscoIpUrpfMIBCompliance':ciscoIpUrpfMIBCompliance,'ciscoIpUrpfMIBGroups':ciscoIpUrpfMIBGroups,_l:ciscoIpUrpfMIBMainObjectGroup,_n:ciscoIpUrpfMIBVrfObjectGroup,_m:ciscoIpUrpfMIBNotifyGroup})