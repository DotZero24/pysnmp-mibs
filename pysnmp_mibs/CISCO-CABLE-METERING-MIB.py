_n='ccmtrMeteringRateCtrlObjGroup'
_m='ccmtrMeteringSrcIntfObjGroup'
_l='ccmtrMeteringObjGroupRev1'
_k='ccmtrMeteringObjGroup'
_j='ccmtrCollectionNotification'
_i='ccmtrCollectionDataTimer'
_h='ccmtrCollectionDataPerSession'
_g='ccmtrCollectionSrcIfIndex'
_f='ccmtrCollectionRevInterval'
_e='ccmtrMeteringNotifEnable'
_d='ccmtrCollectionInterval'
_c='minutes'
_b='ccmtrCollectionID'
_a='Integer32'
_Z='InetAddressType'
_Y='InterfaceIndexOrZero'
_X='ccmtrMeteringNotifGroup'
_W='ccmtrMeteringNotifCtrlGroup'
_V='ccmtrCollectionAggregate'
_U='ccmtrCollectionCpeList'
_T='ccmtrCollectionRowStatus'
_S='ccmtrCollectionSecure'
_R='ccmtrCollectionRetries'
_Q='ccmtrCollectionPort'
_P='ccmtrCollectionIpAddress'
_O='ccmtrCollectionIpAddrType'
_N='ccmtrCollectionFilesystem'
_M='ccmtrCollectionType'
_L='read-only'
_K='deprecated'
_J='SnmpAdminString'
_I='ccmtrCollectionTimestamp'
_H='ccmtrCollectionDestination'
_G='ccmtrCollectionStatus'
_F='read-create'
_E='TruthValue'
_D='Unsigned32'
_C='read-write'
_B='current'
_A='CISCO-CABLE-METERING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_Y)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_Z,'InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_a,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
ciscoCableMeteringMIB=ModuleIdentity((1,3,6,1,4,1,9,9,424))
if mibBuilder.loadTexts:ciscoCableMeteringMIB.setRevisions(('2009-10-13 00:00','2009-05-18 00:00','2004-03-30 00:00'))
class CcmtrStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('success',2),('deviceFull',3),('writeError',4),('fileNotExist',5),('connectionTimeout',6),('dataIncomplete',7)))
class CcmtrCollectionServer(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_CiscoCableMeteringMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCableMeteringMIBNotifs=_CiscoCableMeteringMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,424,0))
_CiscoCableMeteringMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableMeteringMIBObjects=_CiscoCableMeteringMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,424,1))
_CcmtrMeteringConfig_ObjectIdentity=ObjectIdentity
ccmtrMeteringConfig=_CcmtrMeteringConfig_ObjectIdentity((1,3,6,1,4,1,9,9,424,1,1))
class _CcmtrCollectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('local',2),('stream',3),('ipdr',4)))
_CcmtrCollectionType_Type.__name__=_a
_CcmtrCollectionType_Object=MibScalar
ccmtrCollectionType=_CcmtrCollectionType_Object((1,3,6,1,4,1,9,9,424,1,1,1),_CcmtrCollectionType_Type())
ccmtrCollectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionType.setStatus(_B)
class _CcmtrCollectionFilesystem_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CcmtrCollectionFilesystem_Type.__name__=_J
_CcmtrCollectionFilesystem_Object=MibScalar
ccmtrCollectionFilesystem=_CcmtrCollectionFilesystem_Object((1,3,6,1,4,1,9,9,424,1,1,2),_CcmtrCollectionFilesystem_Type())
ccmtrCollectionFilesystem.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionFilesystem.setStatus(_B)
_CcmtrCollectionTable_Object=MibTable
ccmtrCollectionTable=_CcmtrCollectionTable_Object((1,3,6,1,4,1,9,9,424,1,1,3))
if mibBuilder.loadTexts:ccmtrCollectionTable.setStatus(_B)
_CcmtrCollectionEntry_Object=MibTableRow
ccmtrCollectionEntry=_CcmtrCollectionEntry_Object((1,3,6,1,4,1,9,9,424,1,1,3,1))
ccmtrCollectionEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:ccmtrCollectionEntry.setStatus(_B)
_CcmtrCollectionID_Type=CcmtrCollectionServer
_CcmtrCollectionID_Object=MibTableColumn
ccmtrCollectionID=_CcmtrCollectionID_Object((1,3,6,1,4,1,9,9,424,1,1,3,1,1),_CcmtrCollectionID_Type())
ccmtrCollectionID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ccmtrCollectionID.setStatus(_B)
class _CcmtrCollectionIpAddrType_Type(InetAddressType):defaultValue=1
_CcmtrCollectionIpAddrType_Type.__name__=_Z
_CcmtrCollectionIpAddrType_Object=MibTableColumn
ccmtrCollectionIpAddrType=_CcmtrCollectionIpAddrType_Object((1,3,6,1,4,1,9,9,424,1,1,3,1,2),_CcmtrCollectionIpAddrType_Type())
ccmtrCollectionIpAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:ccmtrCollectionIpAddrType.setStatus(_B)
_CcmtrCollectionIpAddress_Type=InetAddress
_CcmtrCollectionIpAddress_Object=MibTableColumn
ccmtrCollectionIpAddress=_CcmtrCollectionIpAddress_Object((1,3,6,1,4,1,9,9,424,1,1,3,1,3),_CcmtrCollectionIpAddress_Type())
ccmtrCollectionIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ccmtrCollectionIpAddress.setStatus(_B)
_CcmtrCollectionPort_Type=InetPortNumber
_CcmtrCollectionPort_Object=MibTableColumn
ccmtrCollectionPort=_CcmtrCollectionPort_Object((1,3,6,1,4,1,9,9,424,1,1,3,1,4),_CcmtrCollectionPort_Type())
ccmtrCollectionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ccmtrCollectionPort.setStatus(_B)
_CcmtrCollectionRowStatus_Type=RowStatus
_CcmtrCollectionRowStatus_Object=MibTableColumn
ccmtrCollectionRowStatus=_CcmtrCollectionRowStatus_Object((1,3,6,1,4,1,9,9,424,1,1,3,1,8),_CcmtrCollectionRowStatus_Type())
ccmtrCollectionRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ccmtrCollectionRowStatus.setStatus(_B)
class _CcmtrCollectionInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,1440))
_CcmtrCollectionInterval_Type.__name__=_D
_CcmtrCollectionInterval_Object=MibScalar
ccmtrCollectionInterval=_CcmtrCollectionInterval_Object((1,3,6,1,4,1,9,9,424,1,1,4),_CcmtrCollectionInterval_Type())
ccmtrCollectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionInterval.setStatus(_K)
if mibBuilder.loadTexts:ccmtrCollectionInterval.setUnits(_c)
class _CcmtrCollectionRetries_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_CcmtrCollectionRetries_Type.__name__=_D
_CcmtrCollectionRetries_Object=MibScalar
ccmtrCollectionRetries=_CcmtrCollectionRetries_Object((1,3,6,1,4,1,9,9,424,1,1,5),_CcmtrCollectionRetries_Type())
ccmtrCollectionRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionRetries.setStatus(_B)
class _CcmtrCollectionSecure_Type(TruthValue):defaultValue=2
_CcmtrCollectionSecure_Type.__name__=_E
_CcmtrCollectionSecure_Object=MibScalar
ccmtrCollectionSecure=_CcmtrCollectionSecure_Object((1,3,6,1,4,1,9,9,424,1,1,6),_CcmtrCollectionSecure_Type())
ccmtrCollectionSecure.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionSecure.setStatus(_B)
class _CcmtrCollectionCpeList_Type(TruthValue):defaultValue=1
_CcmtrCollectionCpeList_Type.__name__=_E
_CcmtrCollectionCpeList_Object=MibScalar
ccmtrCollectionCpeList=_CcmtrCollectionCpeList_Object((1,3,6,1,4,1,9,9,424,1,1,7),_CcmtrCollectionCpeList_Type())
ccmtrCollectionCpeList.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionCpeList.setStatus(_B)
class _CcmtrCollectionAggregate_Type(TruthValue):defaultValue=2
_CcmtrCollectionAggregate_Type.__name__=_E
_CcmtrCollectionAggregate_Object=MibScalar
ccmtrCollectionAggregate=_CcmtrCollectionAggregate_Object((1,3,6,1,4,1,9,9,424,1,1,8),_CcmtrCollectionAggregate_Type())
ccmtrCollectionAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionAggregate.setStatus(_B)
class _CcmtrCollectionSrcIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_CcmtrCollectionSrcIfIndex_Type.__name__=_Y
_CcmtrCollectionSrcIfIndex_Object=MibScalar
ccmtrCollectionSrcIfIndex=_CcmtrCollectionSrcIfIndex_Object((1,3,6,1,4,1,9,9,424,1,1,9),_CcmtrCollectionSrcIfIndex_Type())
ccmtrCollectionSrcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionSrcIfIndex.setStatus(_B)
class _CcmtrCollectionRevInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CcmtrCollectionRevInterval_Type.__name__=_D
_CcmtrCollectionRevInterval_Object=MibScalar
ccmtrCollectionRevInterval=_CcmtrCollectionRevInterval_Object((1,3,6,1,4,1,9,9,424,1,1,10),_CcmtrCollectionRevInterval_Type())
ccmtrCollectionRevInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionRevInterval.setStatus(_B)
if mibBuilder.loadTexts:ccmtrCollectionRevInterval.setUnits(_c)
class _CcmtrCollectionDataPerSession_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,30))
_CcmtrCollectionDataPerSession_Type.__name__=_D
_CcmtrCollectionDataPerSession_Object=MibScalar
ccmtrCollectionDataPerSession=_CcmtrCollectionDataPerSession_Object((1,3,6,1,4,1,9,9,424,1,1,11),_CcmtrCollectionDataPerSession_Type())
ccmtrCollectionDataPerSession.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionDataPerSession.setStatus(_B)
class _CcmtrCollectionDataTimer_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,500))
_CcmtrCollectionDataTimer_Type.__name__=_D
_CcmtrCollectionDataTimer_Object=MibScalar
ccmtrCollectionDataTimer=_CcmtrCollectionDataTimer_Object((1,3,6,1,4,1,9,9,424,1,1,12),_CcmtrCollectionDataTimer_Type())
ccmtrCollectionDataTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrCollectionDataTimer.setStatus(_B)
if mibBuilder.loadTexts:ccmtrCollectionDataTimer.setUnits('milliseconds')
_CcmtrMetering_ObjectIdentity=ObjectIdentity
ccmtrMetering=_CcmtrMetering_ObjectIdentity((1,3,6,1,4,1,9,9,424,1,2))
_CcmtrCollectionStatus_Type=CcmtrStatus
_CcmtrCollectionStatus_Object=MibScalar
ccmtrCollectionStatus=_CcmtrCollectionStatus_Object((1,3,6,1,4,1,9,9,424,1,2,1),_CcmtrCollectionStatus_Type())
ccmtrCollectionStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:ccmtrCollectionStatus.setStatus(_B)
class _CcmtrCollectionDestination_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CcmtrCollectionDestination_Type.__name__=_J
_CcmtrCollectionDestination_Object=MibScalar
ccmtrCollectionDestination=_CcmtrCollectionDestination_Object((1,3,6,1,4,1,9,9,424,1,2,2),_CcmtrCollectionDestination_Type())
ccmtrCollectionDestination.setMaxAccess(_L)
if mibBuilder.loadTexts:ccmtrCollectionDestination.setStatus(_B)
_CcmtrCollectionTimestamp_Type=DateAndTime
_CcmtrCollectionTimestamp_Object=MibScalar
ccmtrCollectionTimestamp=_CcmtrCollectionTimestamp_Object((1,3,6,1,4,1,9,9,424,1,2,3),_CcmtrCollectionTimestamp_Type())
ccmtrCollectionTimestamp.setMaxAccess(_L)
if mibBuilder.loadTexts:ccmtrCollectionTimestamp.setStatus(_B)
class _CcmtrMeteringNotifEnable_Type(TruthValue):defaultValue=2
_CcmtrMeteringNotifEnable_Type.__name__=_E
_CcmtrMeteringNotifEnable_Object=MibScalar
ccmtrMeteringNotifEnable=_CcmtrMeteringNotifEnable_Object((1,3,6,1,4,1,9,9,424,1,2,4),_CcmtrMeteringNotifEnable_Type())
ccmtrMeteringNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmtrMeteringNotifEnable.setStatus(_B)
_CiscoCableMeteringMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCableMeteringMIBConformance=_CiscoCableMeteringMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,424,3))
_CiscoCableMeteringMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCableMeteringMIBCompliances=_CiscoCableMeteringMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,424,3,1))
_CiscoCableMeteringMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCableMeteringMIBGroups=_CiscoCableMeteringMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,424,3,2))
ccmtrMeteringObjGroup=ObjectGroup((1,3,6,1,4,1,9,9,424,3,2,1))
ccmtrMeteringObjGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_d),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ccmtrMeteringObjGroup.setStatus(_K)
ccmtrMeteringNotifCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,424,3,2,2))
ccmtrMeteringNotifCtrlGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:ccmtrMeteringNotifCtrlGroup.setStatus(_B)
ccmtrMeteringObjGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,424,3,2,4))
ccmtrMeteringObjGroupRev1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_T),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_f),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ccmtrMeteringObjGroupRev1.setStatus(_B)
ccmtrMeteringSrcIntfObjGroup=ObjectGroup((1,3,6,1,4,1,9,9,424,3,2,5))
ccmtrMeteringSrcIntfObjGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:ccmtrMeteringSrcIntfObjGroup.setStatus(_B)
ccmtrMeteringRateCtrlObjGroup=ObjectGroup((1,3,6,1,4,1,9,9,424,3,2,6))
ccmtrMeteringRateCtrlObjGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ccmtrMeteringRateCtrlObjGroup.setStatus(_B)
ccmtrCollectionNotification=NotificationType((1,3,6,1,4,1,9,9,424,0,1))
ccmtrCollectionNotification.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ccmtrCollectionNotification.setStatus(_B)
ccmtrMeteringNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,424,3,2,3))
ccmtrMeteringNotifGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:ccmtrMeteringNotifGroup.setStatus(_B)
ciscoCableMeteringCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,424,3,1,1))
ciscoCableMeteringCompliance.setObjects(*((_A,_k),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoCableMeteringCompliance.setStatus(_K)
ciscoCableMeteringComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,424,3,1,2))
ciscoCableMeteringComplianceRev1.setObjects(*((_A,_W),(_A,_X),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoCableMeteringComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CcmtrStatus':CcmtrStatus,'CcmtrCollectionServer':CcmtrCollectionServer,'ciscoCableMeteringMIB':ciscoCableMeteringMIB,'ciscoCableMeteringMIBNotifs':ciscoCableMeteringMIBNotifs,_j:ccmtrCollectionNotification,'ciscoCableMeteringMIBObjects':ciscoCableMeteringMIBObjects,'ccmtrMeteringConfig':ccmtrMeteringConfig,_M:ccmtrCollectionType,_N:ccmtrCollectionFilesystem,'ccmtrCollectionTable':ccmtrCollectionTable,'ccmtrCollectionEntry':ccmtrCollectionEntry,_b:ccmtrCollectionID,_O:ccmtrCollectionIpAddrType,_P:ccmtrCollectionIpAddress,_Q:ccmtrCollectionPort,_T:ccmtrCollectionRowStatus,_d:ccmtrCollectionInterval,_R:ccmtrCollectionRetries,_S:ccmtrCollectionSecure,_U:ccmtrCollectionCpeList,_V:ccmtrCollectionAggregate,_g:ccmtrCollectionSrcIfIndex,_f:ccmtrCollectionRevInterval,_h:ccmtrCollectionDataPerSession,_i:ccmtrCollectionDataTimer,'ccmtrMetering':ccmtrMetering,_G:ccmtrCollectionStatus,_H:ccmtrCollectionDestination,_I:ccmtrCollectionTimestamp,_e:ccmtrMeteringNotifEnable,'ciscoCableMeteringMIBConformance':ciscoCableMeteringMIBConformance,'ciscoCableMeteringMIBCompliances':ciscoCableMeteringMIBCompliances,'ciscoCableMeteringCompliance':ciscoCableMeteringCompliance,'ciscoCableMeteringComplianceRev1':ciscoCableMeteringComplianceRev1,'ciscoCableMeteringMIBGroups':ciscoCableMeteringMIBGroups,_k:ccmtrMeteringObjGroup,_W:ccmtrMeteringNotifCtrlGroup,_X:ccmtrMeteringNotifGroup,_l:ccmtrMeteringObjGroupRev1,_m:ccmtrMeteringSrcIntfObjGroup,_n:ccmtrMeteringRateCtrlObjGroup})