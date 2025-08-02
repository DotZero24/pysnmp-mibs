_P='ciscoDlrMIBNotifyGroup'
_O='ciscoDlrMIBMainObjectGroup'
_N='ciscoDlrRingGatewayStatus'
_M='ciscoDlrRingSupervisorStatus'
_L='ciscoDlrRingStatus'
_K='ciscoDlrRingGatewayDeviceState'
_J='ciscoDlrRingIndex'
_I='ciscoDlrRingGatewayDeviceStatus'
_H='ciscoDlrRingDeviceState'
_G='ciscoDlrRingNetworkStatus'
_F='undefined'
_E='ciscoDlrRingName'
_D='ciscoDlrRingID'
_C='read-only'
_B='current'
_A='CISCO-DLR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDlrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,865))
if mibBuilder.loadTexts:ciscoDlrMIB.setRevisions(('2019-09-11 00:00',))
class DlrNetworkStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('ringNormal',1),('ringFault',2),('ringUnexcpectedLoop',3),('ringPartialFault',4),('ringRapidFaultRestore',5)))
class DlrDeviceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),('supBackup',1),('supActive',2),('normalRing',3),('nonDlr',4)))
class DlrGatewayDeviceStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),('nonGateway',1),('activeGateway',2),('backupGateway',3),('faultGateway',4),('nonSupportedGateway',5),('partialFaultGateway',6)))
class DlrGatewayDeviceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),('gatewayIdle',1),('activeListen',2),('activeNormal',3),('fault',4),('backupNormal',5),('lossUplink',6),('partialNetworkfault',7)))
_CiscoDlrMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDlrMIBNotifs=_CiscoDlrMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,865,0))
_CiscoDlrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDlrMIBObjects=_CiscoDlrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,865,1))
_CiscoDlrRingTable_Object=MibTable
ciscoDlrRingTable=_CiscoDlrRingTable_Object((1,3,6,1,4,1,9,9,865,1,1))
if mibBuilder.loadTexts:ciscoDlrRingTable.setStatus(_B)
_CiscoDlrRingEntry_Object=MibTableRow
ciscoDlrRingEntry=_CiscoDlrRingEntry_Object((1,3,6,1,4,1,9,9,865,1,1,1))
ciscoDlrRingEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:ciscoDlrRingEntry.setStatus(_B)
_CiscoDlrRingIndex_Type=Unsigned32
_CiscoDlrRingIndex_Object=MibTableColumn
ciscoDlrRingIndex=_CiscoDlrRingIndex_Object((1,3,6,1,4,1,9,9,865,1,1,1,1),_CiscoDlrRingIndex_Type())
ciscoDlrRingIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoDlrRingIndex.setStatus(_B)
_CiscoDlrRingID_Type=Unsigned32
_CiscoDlrRingID_Object=MibTableColumn
ciscoDlrRingID=_CiscoDlrRingID_Object((1,3,6,1,4,1,9,9,865,1,1,1,2),_CiscoDlrRingID_Type())
ciscoDlrRingID.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingID.setStatus(_B)
_CiscoDlrRingName_Type=DisplayString
_CiscoDlrRingName_Object=MibTableColumn
ciscoDlrRingName=_CiscoDlrRingName_Object((1,3,6,1,4,1,9,9,865,1,1,1,3),_CiscoDlrRingName_Type())
ciscoDlrRingName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingName.setStatus(_B)
_CiscoDlrRingNetworkStatus_Type=DlrNetworkStatus
_CiscoDlrRingNetworkStatus_Object=MibTableColumn
ciscoDlrRingNetworkStatus=_CiscoDlrRingNetworkStatus_Object((1,3,6,1,4,1,9,9,865,1,1,1,4),_CiscoDlrRingNetworkStatus_Type())
ciscoDlrRingNetworkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingNetworkStatus.setStatus(_B)
_CiscoDlrRingDeviceState_Type=DlrDeviceState
_CiscoDlrRingDeviceState_Object=MibTableColumn
ciscoDlrRingDeviceState=_CiscoDlrRingDeviceState_Object((1,3,6,1,4,1,9,9,865,1,1,1,5),_CiscoDlrRingDeviceState_Type())
ciscoDlrRingDeviceState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingDeviceState.setStatus(_B)
_CiscoDlrRingGatewayDeviceStatus_Type=DlrGatewayDeviceStatus
_CiscoDlrRingGatewayDeviceStatus_Object=MibTableColumn
ciscoDlrRingGatewayDeviceStatus=_CiscoDlrRingGatewayDeviceStatus_Object((1,3,6,1,4,1,9,9,865,1,1,1,6),_CiscoDlrRingGatewayDeviceStatus_Type())
ciscoDlrRingGatewayDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingGatewayDeviceStatus.setStatus(_B)
_CiscoDlrRingGatewayDeviceState_Type=DlrGatewayDeviceState
_CiscoDlrRingGatewayDeviceState_Object=MibTableColumn
ciscoDlrRingGatewayDeviceState=_CiscoDlrRingGatewayDeviceState_Object((1,3,6,1,4,1,9,9,865,1,1,1,7),_CiscoDlrRingGatewayDeviceState_Type())
ciscoDlrRingGatewayDeviceState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoDlrRingGatewayDeviceState.setStatus(_B)
_CiscoDlrMIBConform_ObjectIdentity=ObjectIdentity
ciscoDlrMIBConform=_CiscoDlrMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,865,2))
_CiscoDlrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDlrMIBCompliances=_CiscoDlrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,865,2,1))
_CiscoDlrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDlrMIBGroups=_CiscoDlrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,865,2,2))
ciscoDlrMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,865,2,2,1))
ciscoDlrMIBMainObjectGroup.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_E)))
if mibBuilder.loadTexts:ciscoDlrMIBMainObjectGroup.setStatus(_B)
ciscoDlrRingStatus=NotificationType((1,3,6,1,4,1,9,9,865,0,1))
ciscoDlrRingStatus.setObjects(*((_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:ciscoDlrRingStatus.setStatus(_B)
ciscoDlrRingSupervisorStatus=NotificationType((1,3,6,1,4,1,9,9,865,0,2))
ciscoDlrRingSupervisorStatus.setObjects(*((_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:ciscoDlrRingSupervisorStatus.setStatus(_B)
ciscoDlrRingGatewayStatus=NotificationType((1,3,6,1,4,1,9,9,865,0,3))
ciscoDlrRingGatewayStatus.setObjects(*((_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:ciscoDlrRingGatewayStatus.setStatus(_B)
ciscoDlrMIBNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,865,2,2,2))
ciscoDlrMIBNotifyGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoDlrMIBNotifyGroup.setStatus(_B)
ciscoDlrMIBModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,865,2,1,1))
ciscoDlrMIBModuleCompliance.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoDlrMIBModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DlrNetworkStatus':DlrNetworkStatus,'DlrDeviceState':DlrDeviceState,'DlrGatewayDeviceStatus':DlrGatewayDeviceStatus,'DlrGatewayDeviceState':DlrGatewayDeviceState,'ciscoDlrMIB':ciscoDlrMIB,'ciscoDlrMIBNotifs':ciscoDlrMIBNotifs,_L:ciscoDlrRingStatus,_M:ciscoDlrRingSupervisorStatus,_N:ciscoDlrRingGatewayStatus,'ciscoDlrMIBObjects':ciscoDlrMIBObjects,'ciscoDlrRingTable':ciscoDlrRingTable,'ciscoDlrRingEntry':ciscoDlrRingEntry,_J:ciscoDlrRingIndex,_D:ciscoDlrRingID,_E:ciscoDlrRingName,_G:ciscoDlrRingNetworkStatus,_H:ciscoDlrRingDeviceState,_I:ciscoDlrRingGatewayDeviceStatus,_K:ciscoDlrRingGatewayDeviceState,'ciscoDlrMIBConform':ciscoDlrMIBConform,'ciscoDlrMIBCompliances':ciscoDlrMIBCompliances,'ciscoDlrMIBModuleCompliance':ciscoDlrMIBModuleCompliance,'ciscoDlrMIBGroups':ciscoDlrMIBGroups,_O:ciscoDlrMIBMainObjectGroup,_P:ciscoDlrMIBNotifyGroup})