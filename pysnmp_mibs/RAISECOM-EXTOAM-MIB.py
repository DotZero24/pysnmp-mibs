_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomExtendOam=ModuleIdentity((1,3,6,1,4,1,8886,1,10))
_RaisecomOamExtStatsTable_Object=MibTable
raisecomOamExtStatsTable=_RaisecomOamExtStatsTable_Object((1,3,6,1,4,1,8886,1,10,1))
if mibBuilder.loadTexts:raisecomOamExtStatsTable.setStatus(_A)
_RaisecomOamExtStatsEntry_Object=MibTableRow
raisecomOamExtStatsEntry=_RaisecomOamExtStatsEntry_Object((1,3,6,1,4,1,8886,1,10,1,1))
raisecomOamExtStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:raisecomOamExtStatsEntry.setStatus(_A)
_RaisecomOamExtVariableGetTx_Type=Counter32
_RaisecomOamExtVariableGetTx_Object=MibTableColumn
raisecomOamExtVariableGetTx=_RaisecomOamExtVariableGetTx_Object((1,3,6,1,4,1,8886,1,10,1,1,1),_RaisecomOamExtVariableGetTx_Type())
raisecomOamExtVariableGetTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableGetTx.setStatus(_A)
_RaisecomOamExtVariableGetRx_Type=Counter32
_RaisecomOamExtVariableGetRx_Object=MibTableColumn
raisecomOamExtVariableGetRx=_RaisecomOamExtVariableGetRx_Object((1,3,6,1,4,1,8886,1,10,1,1,2),_RaisecomOamExtVariableGetRx_Type())
raisecomOamExtVariableGetRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableGetRx.setStatus(_A)
_RaisecomOamExtVariableSetTx_Type=Counter32
_RaisecomOamExtVariableSetTx_Object=MibTableColumn
raisecomOamExtVariableSetTx=_RaisecomOamExtVariableSetTx_Object((1,3,6,1,4,1,8886,1,10,1,1,3),_RaisecomOamExtVariableSetTx_Type())
raisecomOamExtVariableSetTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableSetTx.setStatus(_A)
_RaisecomOamExtVariableSetRx_Type=Counter32
_RaisecomOamExtVariableSetRx_Object=MibTableColumn
raisecomOamExtVariableSetRx=_RaisecomOamExtVariableSetRx_Object((1,3,6,1,4,1,8886,1,10,1,1,4),_RaisecomOamExtVariableSetRx_Type())
raisecomOamExtVariableSetRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableSetRx.setStatus(_A)
_RaisecomOamExtVariableGetResponseTx_Type=Counter32
_RaisecomOamExtVariableGetResponseTx_Object=MibTableColumn
raisecomOamExtVariableGetResponseTx=_RaisecomOamExtVariableGetResponseTx_Object((1,3,6,1,4,1,8886,1,10,1,1,5),_RaisecomOamExtVariableGetResponseTx_Type())
raisecomOamExtVariableGetResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableGetResponseTx.setStatus(_A)
_RaisecomOamExtVariableGetResponseRx_Type=Counter32
_RaisecomOamExtVariableGetResponseRx_Object=MibTableColumn
raisecomOamExtVariableGetResponseRx=_RaisecomOamExtVariableGetResponseRx_Object((1,3,6,1,4,1,8886,1,10,1,1,6),_RaisecomOamExtVariableGetResponseRx_Type())
raisecomOamExtVariableGetResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableGetResponseRx.setStatus(_A)
_RaisecomOamExtVariableSetResponseTx_Type=Counter32
_RaisecomOamExtVariableSetResponseTx_Object=MibTableColumn
raisecomOamExtVariableSetResponseTx=_RaisecomOamExtVariableSetResponseTx_Object((1,3,6,1,4,1,8886,1,10,1,1,7),_RaisecomOamExtVariableSetResponseTx_Type())
raisecomOamExtVariableSetResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableSetResponseTx.setStatus(_A)
_RaisecomOamExtVariableSetResponseRx_Type=Counter32
_RaisecomOamExtVariableSetResponseRx_Object=MibTableColumn
raisecomOamExtVariableSetResponseRx=_RaisecomOamExtVariableSetResponseRx_Object((1,3,6,1,4,1,8886,1,10,1,1,8),_RaisecomOamExtVariableSetResponseRx_Type())
raisecomOamExtVariableSetResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtVariableSetResponseRx.setStatus(_A)
_RaisecomOamExtFileReadTx_Type=Counter32
_RaisecomOamExtFileReadTx_Object=MibTableColumn
raisecomOamExtFileReadTx=_RaisecomOamExtFileReadTx_Object((1,3,6,1,4,1,8886,1,10,1,1,9),_RaisecomOamExtFileReadTx_Type())
raisecomOamExtFileReadTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileReadTx.setStatus(_A)
_RaisecomOamExtFileReadRx_Type=Counter32
_RaisecomOamExtFileReadRx_Object=MibTableColumn
raisecomOamExtFileReadRx=_RaisecomOamExtFileReadRx_Object((1,3,6,1,4,1,8886,1,10,1,1,10),_RaisecomOamExtFileReadRx_Type())
raisecomOamExtFileReadRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileReadRx.setStatus(_A)
_RaisecomOamExtFileWriteTx_Type=Counter32
_RaisecomOamExtFileWriteTx_Object=MibTableColumn
raisecomOamExtFileWriteTx=_RaisecomOamExtFileWriteTx_Object((1,3,6,1,4,1,8886,1,10,1,1,11),_RaisecomOamExtFileWriteTx_Type())
raisecomOamExtFileWriteTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileWriteTx.setStatus(_A)
_RaisecomOamExtFileWriteRx_Type=Counter32
_RaisecomOamExtFileWriteRx_Object=MibTableColumn
raisecomOamExtFileWriteRx=_RaisecomOamExtFileWriteRx_Object((1,3,6,1,4,1,8886,1,10,1,1,12),_RaisecomOamExtFileWriteRx_Type())
raisecomOamExtFileWriteRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileWriteRx.setStatus(_A)
_RaisecomOamExtFileTransferDataRx_Type=Counter32
_RaisecomOamExtFileTransferDataRx_Object=MibTableColumn
raisecomOamExtFileTransferDataRx=_RaisecomOamExtFileTransferDataRx_Object((1,3,6,1,4,1,8886,1,10,1,1,13),_RaisecomOamExtFileTransferDataRx_Type())
raisecomOamExtFileTransferDataRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileTransferDataRx.setStatus(_A)
_RaisecomOamExtFileTransferDataTx_Type=Counter32
_RaisecomOamExtFileTransferDataTx_Object=MibTableColumn
raisecomOamExtFileTransferDataTx=_RaisecomOamExtFileTransferDataTx_Object((1,3,6,1,4,1,8886,1,10,1,1,14),_RaisecomOamExtFileTransferDataTx_Type())
raisecomOamExtFileTransferDataTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileTransferDataTx.setStatus(_A)
_RaisecomOamExtFileTransferAckTx_Type=Counter32
_RaisecomOamExtFileTransferAckTx_Object=MibTableColumn
raisecomOamExtFileTransferAckTx=_RaisecomOamExtFileTransferAckTx_Object((1,3,6,1,4,1,8886,1,10,1,1,15),_RaisecomOamExtFileTransferAckTx_Type())
raisecomOamExtFileTransferAckTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileTransferAckTx.setStatus(_A)
_RaisecomOamExtFileTransferAckRx_Type=Counter32
_RaisecomOamExtFileTransferAckRx_Object=MibTableColumn
raisecomOamExtFileTransferAckRx=_RaisecomOamExtFileTransferAckRx_Object((1,3,6,1,4,1,8886,1,10,1,1,16),_RaisecomOamExtFileTransferAckRx_Type())
raisecomOamExtFileTransferAckRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtFileTransferAckRx.setStatus(_A)
_RaisecomOamExtNotificationTx_Type=Counter32
_RaisecomOamExtNotificationTx_Object=MibTableColumn
raisecomOamExtNotificationTx=_RaisecomOamExtNotificationTx_Object((1,3,6,1,4,1,8886,1,10,1,1,17),_RaisecomOamExtNotificationTx_Type())
raisecomOamExtNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtNotificationTx.setStatus(_A)
_RaisecomOamExtNotificationRx_Type=Counter32
_RaisecomOamExtNotificationRx_Object=MibTableColumn
raisecomOamExtNotificationRx=_RaisecomOamExtNotificationRx_Object((1,3,6,1,4,1,8886,1,10,1,1,18),_RaisecomOamExtNotificationRx_Type())
raisecomOamExtNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtNotificationRx.setStatus(_A)
_RaisecomOamExtStaticInfoTx_Type=Counter32
_RaisecomOamExtStaticInfoTx_Object=MibTableColumn
raisecomOamExtStaticInfoTx=_RaisecomOamExtStaticInfoTx_Object((1,3,6,1,4,1,8886,1,10,1,1,19),_RaisecomOamExtStaticInfoTx_Type())
raisecomOamExtStaticInfoTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtStaticInfoTx.setStatus(_A)
_RaisecomOamExtStaticInfoRx_Type=Counter32
_RaisecomOamExtStaticInfoRx_Object=MibTableColumn
raisecomOamExtStaticInfoRx=_RaisecomOamExtStaticInfoRx_Object((1,3,6,1,4,1,8886,1,10,1,1,20),_RaisecomOamExtStaticInfoRx_Type())
raisecomOamExtStaticInfoRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtStaticInfoRx.setStatus(_A)
_RaisecomOamExtDynamicInfoTx_Type=Counter32
_RaisecomOamExtDynamicInfoTx_Object=MibTableColumn
raisecomOamExtDynamicInfoTx=_RaisecomOamExtDynamicInfoTx_Object((1,3,6,1,4,1,8886,1,10,1,1,21),_RaisecomOamExtDynamicInfoTx_Type())
raisecomOamExtDynamicInfoTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtDynamicInfoTx.setStatus(_A)
_RaisecomOamExtDynamicInfoRx_Type=Counter32
_RaisecomOamExtDynamicInfoRx_Object=MibTableColumn
raisecomOamExtDynamicInfoRx=_RaisecomOamExtDynamicInfoRx_Object((1,3,6,1,4,1,8886,1,10,1,1,22),_RaisecomOamExtDynamicInfoRx_Type())
raisecomOamExtDynamicInfoRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtDynamicInfoRx.setStatus(_A)
_RaisecomOamExtConfTx_Type=Counter32
_RaisecomOamExtConfTx_Object=MibTableColumn
raisecomOamExtConfTx=_RaisecomOamExtConfTx_Object((1,3,6,1,4,1,8886,1,10,1,1,23),_RaisecomOamExtConfTx_Type())
raisecomOamExtConfTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtConfTx.setStatus(_A)
_RaisecomOamExtConfRx_Type=Counter32
_RaisecomOamExtConfRx_Object=MibTableColumn
raisecomOamExtConfRx=_RaisecomOamExtConfRx_Object((1,3,6,1,4,1,8886,1,10,1,1,24),_RaisecomOamExtConfRx_Type())
raisecomOamExtConfRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtConfRx.setStatus(_A)
_RaisecomOamExtCmdTx_Type=Counter32
_RaisecomOamExtCmdTx_Object=MibTableColumn
raisecomOamExtCmdTx=_RaisecomOamExtCmdTx_Object((1,3,6,1,4,1,8886,1,10,1,1,25),_RaisecomOamExtCmdTx_Type())
raisecomOamExtCmdTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtCmdTx.setStatus(_A)
_RaisecomOamExtCmdRx_Type=Counter32
_RaisecomOamExtCmdRx_Object=MibTableColumn
raisecomOamExtCmdRx=_RaisecomOamExtCmdRx_Object((1,3,6,1,4,1,8886,1,10,1,1,26),_RaisecomOamExtCmdRx_Type())
raisecomOamExtCmdRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtCmdRx.setStatus(_A)
_RaisecomOamExtConnectTx_Type=Counter32
_RaisecomOamExtConnectTx_Object=MibTableColumn
raisecomOamExtConnectTx=_RaisecomOamExtConnectTx_Object((1,3,6,1,4,1,8886,1,10,1,1,27),_RaisecomOamExtConnectTx_Type())
raisecomOamExtConnectTx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtConnectTx.setStatus(_A)
_RaisecomOamExtConnectRx_Type=Counter32
_RaisecomOamExtConnectRx_Object=MibTableColumn
raisecomOamExtConnectRx=_RaisecomOamExtConnectRx_Object((1,3,6,1,4,1,8886,1,10,1,1,28),_RaisecomOamExtConnectRx_Type())
raisecomOamExtConnectRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtConnectRx.setStatus(_A)
_RaisecomOamExtUnknownRx_Type=Counter32
_RaisecomOamExtUnknownRx_Object=MibTableColumn
raisecomOamExtUnknownRx=_RaisecomOamExtUnknownRx_Object((1,3,6,1,4,1,8886,1,10,1,1,29),_RaisecomOamExtUnknownRx_Type())
raisecomOamExtUnknownRx.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtUnknownRx.setStatus(_A)
_RaisecomOamExtStatusTable_Object=MibTable
raisecomOamExtStatusTable=_RaisecomOamExtStatusTable_Object((1,3,6,1,4,1,8886,1,10,2))
if mibBuilder.loadTexts:raisecomOamExtStatusTable.setStatus(_A)
_RaisecomOamExtStatusEntry_Object=MibTableRow
raisecomOamExtStatusEntry=_RaisecomOamExtStatusEntry_Object((1,3,6,1,4,1,8886,1,10,2,1))
raisecomOamExtStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:raisecomOamExtStatusEntry.setStatus(_A)
class _RaisecomOamExtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonoperative',1),('invariableInfoGet',2),('invariableInfoGetError',3),('operational',4),('fileTransfer',5)))
_RaisecomOamExtStatus_Type.__name__=_E
_RaisecomOamExtStatus_Object=MibTableColumn
raisecomOamExtStatus=_RaisecomOamExtStatus_Object((1,3,6,1,4,1,8886,1,10,2,1,1),_RaisecomOamExtStatus_Type())
raisecomOamExtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomOamExtStatus.setStatus(_A)
_RaisecomOamExtRemoteMibObjects_ObjectIdentity=ObjectIdentity
raisecomOamExtRemoteMibObjects=_RaisecomOamExtRemoteMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,10,3))
_RaisecomOamNotificationEnable_Type=EnableVar
_RaisecomOamNotificationEnable_Object=MibScalar
raisecomOamNotificationEnable=_RaisecomOamNotificationEnable_Object((1,3,6,1,4,1,8886,1,10,3,1),_RaisecomOamNotificationEnable_Type())
raisecomOamNotificationEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomOamNotificationEnable.setStatus(_A)
_RaisecomOamExtConfigReqEnable_Type=EnableVar
_RaisecomOamExtConfigReqEnable_Object=MibScalar
raisecomOamExtConfigReqEnable=_RaisecomOamExtConfigReqEnable_Object((1,3,6,1,4,1,8886,1,10,3,2),_RaisecomOamExtConfigReqEnable_Type())
raisecomOamExtConfigReqEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomOamExtConfigReqEnable.setStatus(_A)
mibBuilder.exportSymbols('RAISECOM-EXTOAM-MIB',**{'raisecomExtendOam':raisecomExtendOam,'raisecomOamExtStatsTable':raisecomOamExtStatsTable,'raisecomOamExtStatsEntry':raisecomOamExtStatsEntry,'raisecomOamExtVariableGetTx':raisecomOamExtVariableGetTx,'raisecomOamExtVariableGetRx':raisecomOamExtVariableGetRx,'raisecomOamExtVariableSetTx':raisecomOamExtVariableSetTx,'raisecomOamExtVariableSetRx':raisecomOamExtVariableSetRx,'raisecomOamExtVariableGetResponseTx':raisecomOamExtVariableGetResponseTx,'raisecomOamExtVariableGetResponseRx':raisecomOamExtVariableGetResponseRx,'raisecomOamExtVariableSetResponseTx':raisecomOamExtVariableSetResponseTx,'raisecomOamExtVariableSetResponseRx':raisecomOamExtVariableSetResponseRx,'raisecomOamExtFileReadTx':raisecomOamExtFileReadTx,'raisecomOamExtFileReadRx':raisecomOamExtFileReadRx,'raisecomOamExtFileWriteTx':raisecomOamExtFileWriteTx,'raisecomOamExtFileWriteRx':raisecomOamExtFileWriteRx,'raisecomOamExtFileTransferDataRx':raisecomOamExtFileTransferDataRx,'raisecomOamExtFileTransferDataTx':raisecomOamExtFileTransferDataTx,'raisecomOamExtFileTransferAckTx':raisecomOamExtFileTransferAckTx,'raisecomOamExtFileTransferAckRx':raisecomOamExtFileTransferAckRx,'raisecomOamExtNotificationTx':raisecomOamExtNotificationTx,'raisecomOamExtNotificationRx':raisecomOamExtNotificationRx,'raisecomOamExtStaticInfoTx':raisecomOamExtStaticInfoTx,'raisecomOamExtStaticInfoRx':raisecomOamExtStaticInfoRx,'raisecomOamExtDynamicInfoTx':raisecomOamExtDynamicInfoTx,'raisecomOamExtDynamicInfoRx':raisecomOamExtDynamicInfoRx,'raisecomOamExtConfTx':raisecomOamExtConfTx,'raisecomOamExtConfRx':raisecomOamExtConfRx,'raisecomOamExtCmdTx':raisecomOamExtCmdTx,'raisecomOamExtCmdRx':raisecomOamExtCmdRx,'raisecomOamExtConnectTx':raisecomOamExtConnectTx,'raisecomOamExtConnectRx':raisecomOamExtConnectRx,'raisecomOamExtUnknownRx':raisecomOamExtUnknownRx,'raisecomOamExtStatusTable':raisecomOamExtStatusTable,'raisecomOamExtStatusEntry':raisecomOamExtStatusEntry,'raisecomOamExtStatus':raisecomOamExtStatus,'raisecomOamExtRemoteMibObjects':raisecomOamExtRemoteMibObjects,'raisecomOamNotificationEnable':raisecomOamNotificationEnable,'raisecomOamExtConfigReqEnable':raisecomOamExtConfigReqEnable})