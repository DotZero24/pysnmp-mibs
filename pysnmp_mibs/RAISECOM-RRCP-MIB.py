_K='not-accessible'
_J='rcRrcpDeviceType'
_I='rcRrcpDeviceId'
_H='Integer32'
_G='OctetString'
_F='rcRrcpMacAddress'
_E='rcRrcpInterfaceIndex'
_D='read-write'
_C='RAISECOM-RRCP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rcRrcp,=mibBuilder.importSymbols('RAISECOM-RRCP-VLAN-MIB','rcRrcp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcRrcpProtocol=ModuleIdentity((1,3,6,1,4,1,8886,6,1,52,1))
if mibBuilder.loadTexts:rcRrcpProtocol.setRevisions(('2010-04-09 00:00','2009-07-06 00:00'))
_RcRrcpMibNotifications_ObjectIdentity=ObjectIdentity
rcRrcpMibNotifications=_RcRrcpMibNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,52,1,1))
_RcRrcpMibObjects_ObjectIdentity=ObjectIdentity
rcRrcpMibObjects=_RcRrcpMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,52,1,2))
_RcRrcpGlobalGroup_ObjectIdentity=ObjectIdentity
rcRrcpGlobalGroup=_RcRrcpGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,52,1,2,1))
_RcRrcpCurrentNumDevices_Type=Integer32
_RcRrcpCurrentNumDevices_Object=MibScalar
rcRrcpCurrentNumDevices=_RcRrcpCurrentNumDevices_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,1),_RcRrcpCurrentNumDevices_Type())
rcRrcpCurrentNumDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpCurrentNumDevices.setStatus(_A)
_RcRrcpNumDevices_Type=Integer32
_RcRrcpNumDevices_Object=MibScalar
rcRrcpNumDevices=_RcRrcpNumDevices_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,2),_RcRrcpNumDevices_Type())
rcRrcpNumDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpNumDevices.setStatus(_A)
_RcRrcpTrapEnable_Type=EnableVar
_RcRrcpTrapEnable_Object=MibScalar
rcRrcpTrapEnable=_RcRrcpTrapEnable_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,3),_RcRrcpTrapEnable_Type())
rcRrcpTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpTrapEnable.setStatus(_A)
class _RcRrcpHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcRrcpHelloTime_Type.__name__=_H
_RcRrcpHelloTime_Object=MibScalar
rcRrcpHelloTime=_RcRrcpHelloTime_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,4),_RcRrcpHelloTime_Type())
rcRrcpHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:rcRrcpHelloTime.setUnits('minutes')
_RcRrcpDeviceUpdate_Type=TruthValue
_RcRrcpDeviceUpdate_Object=MibScalar
rcRrcpDeviceUpdate=_RcRrcpDeviceUpdate_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,5),_RcRrcpDeviceUpdate_Type())
rcRrcpDeviceUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpDeviceUpdate.setStatus(_A)
_RcRrcpStatsClear_Type=TruthValue
_RcRrcpStatsClear_Object=MibScalar
rcRrcpStatsClear=_RcRrcpStatsClear_Object((1,3,6,1,4,1,8886,6,1,52,1,2,1,6),_RcRrcpStatsClear_Type())
rcRrcpStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpStatsClear.setStatus(_A)
_RcRrcpCopyGroup_ObjectIdentity=ObjectIdentity
rcRrcpCopyGroup=_RcRrcpCopyGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,52,1,2,2))
_RcRrcpSourceDeviceId_Type=Integer32
_RcRrcpSourceDeviceId_Object=MibScalar
rcRrcpSourceDeviceId=_RcRrcpSourceDeviceId_Object((1,3,6,1,4,1,8886,6,1,52,1,2,2,1),_RcRrcpSourceDeviceId_Type())
rcRrcpSourceDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpSourceDeviceId.setStatus(_A)
_RcRrcpDestinationDeviceList_Type=OctetString
_RcRrcpDestinationDeviceList_Object=MibScalar
rcRrcpDestinationDeviceList=_RcRrcpDestinationDeviceList_Object((1,3,6,1,4,1,8886,6,1,52,1,2,2,2),_RcRrcpDestinationDeviceList_Type())
rcRrcpDestinationDeviceList.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpDestinationDeviceList.setStatus(_A)
class _RcRrcpCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('busy',2),('completed',3),('error',4)))
_RcRrcpCopyStatus_Type.__name__=_H
_RcRrcpCopyStatus_Object=MibScalar
rcRrcpCopyStatus=_RcRrcpCopyStatus_Object((1,3,6,1,4,1,8886,6,1,52,1,2,2,3),_RcRrcpCopyStatus_Type())
rcRrcpCopyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpCopyStatus.setStatus(_A)
_RcRrcpCopyFailDeviceList_Type=OctetString
_RcRrcpCopyFailDeviceList_Object=MibScalar
rcRrcpCopyFailDeviceList=_RcRrcpCopyFailDeviceList_Object((1,3,6,1,4,1,8886,6,1,52,1,2,2,4),_RcRrcpCopyFailDeviceList_Type())
rcRrcpCopyFailDeviceList.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpCopyFailDeviceList.setStatus(_A)
_RcRrcpInterfaceTable_Object=MibTable
rcRrcpInterfaceTable=_RcRrcpInterfaceTable_Object((1,3,6,1,4,1,8886,6,1,52,1,2,3))
if mibBuilder.loadTexts:rcRrcpInterfaceTable.setStatus(_A)
_RcRrcpInterfaceEntry_Object=MibTableRow
rcRrcpInterfaceEntry=_RcRrcpInterfaceEntry_Object((1,3,6,1,4,1,8886,6,1,52,1,2,3,1))
rcRrcpInterfaceEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:rcRrcpInterfaceEntry.setStatus(_A)
_RcRrcpInterfaceIndex_Type=Integer32
_RcRrcpInterfaceIndex_Object=MibTableColumn
rcRrcpInterfaceIndex=_RcRrcpInterfaceIndex_Object((1,3,6,1,4,1,8886,6,1,52,1,2,3,1,1),_RcRrcpInterfaceIndex_Type())
rcRrcpInterfaceIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcRrcpInterfaceIndex.setStatus(_A)
class _RcRrcpInterfaceDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RcRrcpInterfaceDescription_Type.__name__=_G
_RcRrcpInterfaceDescription_Object=MibTableColumn
rcRrcpInterfaceDescription=_RcRrcpInterfaceDescription_Object((1,3,6,1,4,1,8886,6,1,52,1,2,3,1,2),_RcRrcpInterfaceDescription_Type())
rcRrcpInterfaceDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpInterfaceDescription.setStatus(_A)
_RcRrcpInterfaceEnable_Type=EnableVar
_RcRrcpInterfaceEnable_Object=MibTableColumn
rcRrcpInterfaceEnable=_RcRrcpInterfaceEnable_Object((1,3,6,1,4,1,8886,6,1,52,1,2,3,1,3),_RcRrcpInterfaceEnable_Type())
rcRrcpInterfaceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcRrcpInterfaceEnable.setStatus(_A)
_RcRrcpDeviceTable_Object=MibTable
rcRrcpDeviceTable=_RcRrcpDeviceTable_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4))
if mibBuilder.loadTexts:rcRrcpDeviceTable.setStatus(_A)
_RcRrcpDeviceEntry_Object=MibTableRow
rcRrcpDeviceEntry=_RcRrcpDeviceEntry_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1))
rcRrcpDeviceEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:rcRrcpDeviceEntry.setStatus(_A)
_RcRrcpMacAddress_Type=MacAddress
_RcRrcpMacAddress_Object=MibTableColumn
rcRrcpMacAddress=_RcRrcpMacAddress_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,1),_RcRrcpMacAddress_Type())
rcRrcpMacAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:rcRrcpMacAddress.setStatus(_A)
_RcRrcpDeviceId_Type=Integer32
_RcRrcpDeviceId_Object=MibTableColumn
rcRrcpDeviceId=_RcRrcpDeviceId_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,2),_RcRrcpDeviceId_Type())
rcRrcpDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpDeviceId.setStatus(_A)
class _RcRrcpDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcRrcpDeviceType_Type.__name__=_G
_RcRrcpDeviceType_Object=MibTableColumn
rcRrcpDeviceType=_RcRrcpDeviceType_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,3),_RcRrcpDeviceType_Type())
rcRrcpDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpDeviceType.setStatus(_A)
_RcRrcpDownlinkPort_Type=Integer32
_RcRrcpDownlinkPort_Object=MibTableColumn
rcRrcpDownlinkPort=_RcRrcpDownlinkPort_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,4),_RcRrcpDownlinkPort_Type())
rcRrcpDownlinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpDownlinkPort.setStatus(_A)
_RcRrcpUplinkPort_Type=Integer32
_RcRrcpUplinkPort_Object=MibTableColumn
rcRrcpUplinkPort=_RcRrcpUplinkPort_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,5),_RcRrcpUplinkPort_Type())
rcRrcpUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpUplinkPort.setStatus(_A)
_RcRrcpUplinkMac_Type=MacAddress
_RcRrcpUplinkMac_Object=MibTableColumn
rcRrcpUplinkMac=_RcRrcpUplinkMac_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,6),_RcRrcpUplinkMac_Type())
rcRrcpUplinkMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpUplinkMac.setStatus(_A)
_RcRrcpSoftVersion_Type=Integer32
_RcRrcpSoftVersion_Object=MibTableColumn
rcRrcpSoftVersion=_RcRrcpSoftVersion_Object((1,3,6,1,4,1,8886,6,1,52,1,2,4,1,7),_RcRrcpSoftVersion_Type())
rcRrcpSoftVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpSoftVersion.setStatus(_A)
_RcRrcpStatsTable_Object=MibTable
rcRrcpStatsTable=_RcRrcpStatsTable_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5))
if mibBuilder.loadTexts:rcRrcpStatsTable.setStatus(_A)
_RcRrcpStatsEntry_Object=MibTableRow
rcRrcpStatsEntry=_RcRrcpStatsEntry_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1))
rcRrcpStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:rcRrcpStatsEntry.setStatus(_A)
_RcRrcpHelloTx_Type=Counter32
_RcRrcpHelloTx_Object=MibTableColumn
rcRrcpHelloTx=_RcRrcpHelloTx_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1,1),_RcRrcpHelloTx_Type())
rcRrcpHelloTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpHelloTx.setStatus(_A)
_RcRrcpGetTx_Type=Counter32
_RcRrcpGetTx_Object=MibTableColumn
rcRrcpGetTx=_RcRrcpGetTx_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1,2),_RcRrcpGetTx_Type())
rcRrcpGetTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpGetTx.setStatus(_A)
_RcRrcpSetTx_Type=Counter32
_RcRrcpSetTx_Object=MibTableColumn
rcRrcpSetTx=_RcRrcpSetTx_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1,3),_RcRrcpSetTx_Type())
rcRrcpSetTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpSetTx.setStatus(_A)
_RcRrcpGetReplyRx_Type=Counter32
_RcRrcpGetReplyRx_Object=MibTableColumn
rcRrcpGetReplyRx=_RcRrcpGetReplyRx_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1,4),_RcRrcpGetReplyRx_Type())
rcRrcpGetReplyRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpGetReplyRx.setStatus(_A)
_RcRrcpHelloReplyRx_Type=Counter32
_RcRrcpHelloReplyRx_Object=MibTableColumn
rcRrcpHelloReplyRx=_RcRrcpHelloReplyRx_Object((1,3,6,1,4,1,8886,6,1,52,1,2,5,1,5),_RcRrcpHelloReplyRx_Type())
rcRrcpHelloReplyRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRrcpHelloReplyRx.setStatus(_A)
rcRrcpDeviceUp=NotificationType((1,3,6,1,4,1,8886,6,1,52,1,1,1))
rcRrcpDeviceUp.setObjects(*((_C,_E),(_C,_F),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:rcRrcpDeviceUp.setStatus(_A)
rcRrcpDeviceDown=NotificationType((1,3,6,1,4,1,8886,6,1,52,1,1,2))
rcRrcpDeviceDown.setObjects(*((_C,_E),(_C,_F),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:rcRrcpDeviceDown.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcRrcpProtocol':rcRrcpProtocol,'rcRrcpMibNotifications':rcRrcpMibNotifications,'rcRrcpDeviceUp':rcRrcpDeviceUp,'rcRrcpDeviceDown':rcRrcpDeviceDown,'rcRrcpMibObjects':rcRrcpMibObjects,'rcRrcpGlobalGroup':rcRrcpGlobalGroup,'rcRrcpCurrentNumDevices':rcRrcpCurrentNumDevices,'rcRrcpNumDevices':rcRrcpNumDevices,'rcRrcpTrapEnable':rcRrcpTrapEnable,'rcRrcpHelloTime':rcRrcpHelloTime,'rcRrcpDeviceUpdate':rcRrcpDeviceUpdate,'rcRrcpStatsClear':rcRrcpStatsClear,'rcRrcpCopyGroup':rcRrcpCopyGroup,'rcRrcpSourceDeviceId':rcRrcpSourceDeviceId,'rcRrcpDestinationDeviceList':rcRrcpDestinationDeviceList,'rcRrcpCopyStatus':rcRrcpCopyStatus,'rcRrcpCopyFailDeviceList':rcRrcpCopyFailDeviceList,'rcRrcpInterfaceTable':rcRrcpInterfaceTable,'rcRrcpInterfaceEntry':rcRrcpInterfaceEntry,_E:rcRrcpInterfaceIndex,'rcRrcpInterfaceDescription':rcRrcpInterfaceDescription,'rcRrcpInterfaceEnable':rcRrcpInterfaceEnable,'rcRrcpDeviceTable':rcRrcpDeviceTable,'rcRrcpDeviceEntry':rcRrcpDeviceEntry,_F:rcRrcpMacAddress,_I:rcRrcpDeviceId,_J:rcRrcpDeviceType,'rcRrcpDownlinkPort':rcRrcpDownlinkPort,'rcRrcpUplinkPort':rcRrcpUplinkPort,'rcRrcpUplinkMac':rcRrcpUplinkMac,'rcRrcpSoftVersion':rcRrcpSoftVersion,'rcRrcpStatsTable':rcRrcpStatsTable,'rcRrcpStatsEntry':rcRrcpStatsEntry,'rcRrcpHelloTx':rcRrcpHelloTx,'rcRrcpGetTx':rcRrcpGetTx,'rcRrcpSetTx':rcRrcpSetTx,'rcRrcpGetReplyRx':rcRrcpGetReplyRx,'rcRrcpHelloReplyRx':rcRrcpHelloReplyRx})