_k='qtechWlogNotifyStaOperReason'
_j='qtechWlogNotifyStaAbnormalOperType'
_i='qtechWlogNotifyStaOperType'
_h='qtechWlogNotifySsid'
_g='qtechWlogNotifyStaLinkrate'
_f='qtechWlogNotifyStaRssi'
_e='qtechWlogNotifyApRadioD1xStaNum'
_d='qtechWlogNotifyApRadioWebStaNum'
_c='qtechWlogNotifyApRadioTotalStaNum'
_b='qtechWlogNotifyApRadioRetrsmit'
_a='qtechWlogNotifyApRadioErrFrame'
_Z='qtechWlogNotifyApRadioRssi'
_Y='qtechWlogNotifyApRadioPower'
_X='qtechWlogNotifyApRadioWorkChnl'
_W='qtechWlogNotifyApIntfErrorOutputPkts'
_V='qtechWlogNotifyApIntfErrorInputPkts'
_U='qtechWlogNotifyApIntfBroadcastOutputPkts'
_T='qtechWlogNotifyApIntfBroadcastInputPkts'
_S='qtechWlogNotifyApIntfMulticastOutputPkts'
_R='qtechWlogNotifyApIntfMulticastInputPkts'
_Q='qtechWlogNotifyApIntfUnicastOutputPkts'
_P='qtechWlogNotifyApIntfUnicastInputPkts'
_O='qtechWlogNotifyApIntfOutputRate'
_N='qtechWlogNotifyApIntfInputRate'
_M='qtechWlogNotifyApCwDownReason'
_L='qtechWlogNotifyStaIpv6'
_K='qtechWlogNotifyStaIp'
_J='qtechWlogNotifyStaMac'
_I='qtechWlogNotifyApRadioId'
_H='qtechWlogNotifyApIntfName'
_G='qtechWlogNotifyApCwDownId'
_F='qtechWlogNotifyApIp'
_E='qtechWlogNotifyApMac'
_D='qtechWlogNotifyApName'
_C='accessible-for-notify'
_B='current'
_A='QTECH-WLAN-WLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechWlanWlogMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,118))
if mibBuilder.loadTexts:qtechWlanWlogMIB.setRevisions(('2012-10-10 00:00',))
_QtechWlanWlogNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
qtechWlanWlogNotificationsMIBObjects=_QtechWlanWlogNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,118,1))
_QtechWlanWlogNtfObjects_ObjectIdentity=ObjectIdentity
qtechWlanWlogNtfObjects=_QtechWlanWlogNtfObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,118,1,1))
_QtechWlogNotifyApName_Type=DisplayString
_QtechWlogNotifyApName_Object=MibScalar
qtechWlogNotifyApName=_QtechWlogNotifyApName_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,1),_QtechWlogNotifyApName_Type())
qtechWlogNotifyApName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApName.setStatus(_B)
_QtechWlogNotifyApMac_Type=MacAddress
_QtechWlogNotifyApMac_Object=MibScalar
qtechWlogNotifyApMac=_QtechWlogNotifyApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,2),_QtechWlogNotifyApMac_Type())
qtechWlogNotifyApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApMac.setStatus(_B)
_QtechWlogNotifyApIp_Type=InetAddress
_QtechWlogNotifyApIp_Object=MibScalar
qtechWlogNotifyApIp=_QtechWlogNotifyApIp_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,3),_QtechWlogNotifyApIp_Type())
qtechWlogNotifyApIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIp.setStatus(_B)
_QtechWlogNotifyApCwDownId_Type=Integer32
_QtechWlogNotifyApCwDownId_Object=MibScalar
qtechWlogNotifyApCwDownId=_QtechWlogNotifyApCwDownId_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,4),_QtechWlogNotifyApCwDownId_Type())
qtechWlogNotifyApCwDownId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApCwDownId.setStatus(_B)
_QtechWlogNotifyApCwDownReason_Type=DisplayString
_QtechWlogNotifyApCwDownReason_Object=MibScalar
qtechWlogNotifyApCwDownReason=_QtechWlogNotifyApCwDownReason_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,5),_QtechWlogNotifyApCwDownReason_Type())
qtechWlogNotifyApCwDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApCwDownReason.setStatus(_B)
_QtechWlogNotifyApIntfStatTable_Object=MibTable
qtechWlogNotifyApIntfStatTable=_QtechWlogNotifyApIntfStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6))
if mibBuilder.loadTexts:qtechWlogNotifyApIntfStatTable.setStatus(_B)
_QtechWlogNotifyApIntfStatEntry_Object=MibTableRow
qtechWlogNotifyApIntfStatEntry=_QtechWlogNotifyApIntfStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1))
qtechWlogNotifyApIntfStatEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:qtechWlogNotifyApIntfStatEntry.setStatus(_B)
_QtechWlogNotifyApIntfName_Type=DisplayString
_QtechWlogNotifyApIntfName_Object=MibTableColumn
qtechWlogNotifyApIntfName=_QtechWlogNotifyApIntfName_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,1),_QtechWlogNotifyApIntfName_Type())
qtechWlogNotifyApIntfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfName.setStatus(_B)
_QtechWlogNotifyApIntfInputRate_Type=Integer32
_QtechWlogNotifyApIntfInputRate_Object=MibTableColumn
qtechWlogNotifyApIntfInputRate=_QtechWlogNotifyApIntfInputRate_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,2),_QtechWlogNotifyApIntfInputRate_Type())
qtechWlogNotifyApIntfInputRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfInputRate.setStatus(_B)
_QtechWlogNotifyApIntfOutputRate_Type=Integer32
_QtechWlogNotifyApIntfOutputRate_Object=MibTableColumn
qtechWlogNotifyApIntfOutputRate=_QtechWlogNotifyApIntfOutputRate_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,3),_QtechWlogNotifyApIntfOutputRate_Type())
qtechWlogNotifyApIntfOutputRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfOutputRate.setStatus(_B)
_QtechWlogNotifyApIntfUnicastInputPkts_Type=Integer32
_QtechWlogNotifyApIntfUnicastInputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfUnicastInputPkts=_QtechWlogNotifyApIntfUnicastInputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,4),_QtechWlogNotifyApIntfUnicastInputPkts_Type())
qtechWlogNotifyApIntfUnicastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfUnicastInputPkts.setStatus(_B)
_QtechWlogNotifyApIntfUnicastOutputPkts_Type=Integer32
_QtechWlogNotifyApIntfUnicastOutputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfUnicastOutputPkts=_QtechWlogNotifyApIntfUnicastOutputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,5),_QtechWlogNotifyApIntfUnicastOutputPkts_Type())
qtechWlogNotifyApIntfUnicastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfUnicastOutputPkts.setStatus(_B)
_QtechWlogNotifyApIntfMulticastInputPkts_Type=Integer32
_QtechWlogNotifyApIntfMulticastInputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfMulticastInputPkts=_QtechWlogNotifyApIntfMulticastInputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,6),_QtechWlogNotifyApIntfMulticastInputPkts_Type())
qtechWlogNotifyApIntfMulticastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfMulticastInputPkts.setStatus(_B)
_QtechWlogNotifyApIntfMulticastOutputPkts_Type=Integer32
_QtechWlogNotifyApIntfMulticastOutputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfMulticastOutputPkts=_QtechWlogNotifyApIntfMulticastOutputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,7),_QtechWlogNotifyApIntfMulticastOutputPkts_Type())
qtechWlogNotifyApIntfMulticastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfMulticastOutputPkts.setStatus(_B)
_QtechWlogNotifyApIntfBroadcastInputPkts_Type=Integer32
_QtechWlogNotifyApIntfBroadcastInputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfBroadcastInputPkts=_QtechWlogNotifyApIntfBroadcastInputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,8),_QtechWlogNotifyApIntfBroadcastInputPkts_Type())
qtechWlogNotifyApIntfBroadcastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfBroadcastInputPkts.setStatus(_B)
_QtechWlogNotifyApIntfBroadcastOutputPkts_Type=Integer32
_QtechWlogNotifyApIntfBroadcastOutputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfBroadcastOutputPkts=_QtechWlogNotifyApIntfBroadcastOutputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,9),_QtechWlogNotifyApIntfBroadcastOutputPkts_Type())
qtechWlogNotifyApIntfBroadcastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfBroadcastOutputPkts.setStatus(_B)
_QtechWlogNotifyApIntfErrorInputPkts_Type=Integer32
_QtechWlogNotifyApIntfErrorInputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfErrorInputPkts=_QtechWlogNotifyApIntfErrorInputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,10),_QtechWlogNotifyApIntfErrorInputPkts_Type())
qtechWlogNotifyApIntfErrorInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfErrorInputPkts.setStatus(_B)
_QtechWlogNotifyApIntfErrorOutputPkts_Type=Integer32
_QtechWlogNotifyApIntfErrorOutputPkts_Object=MibTableColumn
qtechWlogNotifyApIntfErrorOutputPkts=_QtechWlogNotifyApIntfErrorOutputPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,6,1,11),_QtechWlogNotifyApIntfErrorOutputPkts_Type())
qtechWlogNotifyApIntfErrorOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApIntfErrorOutputPkts.setStatus(_B)
_QtechWlogNotifyApRadioStatTable_Object=MibTable
qtechWlogNotifyApRadioStatTable=_QtechWlogNotifyApRadioStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7))
if mibBuilder.loadTexts:qtechWlogNotifyApRadioStatTable.setStatus(_B)
_QtechWlogNotifyApRadioStatEntry_Object=MibTableRow
qtechWlogNotifyApRadioStatEntry=_QtechWlogNotifyApRadioStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1))
qtechWlogNotifyApRadioStatEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:qtechWlogNotifyApRadioStatEntry.setStatus(_B)
_QtechWlogNotifyApRadioId_Type=Integer32
_QtechWlogNotifyApRadioId_Object=MibTableColumn
qtechWlogNotifyApRadioId=_QtechWlogNotifyApRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,1),_QtechWlogNotifyApRadioId_Type())
qtechWlogNotifyApRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioId.setStatus(_B)
_QtechWlogNotifyApRadioWorkChnl_Type=Integer32
_QtechWlogNotifyApRadioWorkChnl_Object=MibTableColumn
qtechWlogNotifyApRadioWorkChnl=_QtechWlogNotifyApRadioWorkChnl_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,2),_QtechWlogNotifyApRadioWorkChnl_Type())
qtechWlogNotifyApRadioWorkChnl.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioWorkChnl.setStatus(_B)
_QtechWlogNotifyApRadioPower_Type=Integer32
_QtechWlogNotifyApRadioPower_Object=MibTableColumn
qtechWlogNotifyApRadioPower=_QtechWlogNotifyApRadioPower_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,3),_QtechWlogNotifyApRadioPower_Type())
qtechWlogNotifyApRadioPower.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioPower.setStatus(_B)
_QtechWlogNotifyApRadioRssi_Type=Integer32
_QtechWlogNotifyApRadioRssi_Object=MibTableColumn
qtechWlogNotifyApRadioRssi=_QtechWlogNotifyApRadioRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,4),_QtechWlogNotifyApRadioRssi_Type())
qtechWlogNotifyApRadioRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioRssi.setStatus(_B)
_QtechWlogNotifyApRadioErrFrame_Type=Integer32
_QtechWlogNotifyApRadioErrFrame_Object=MibTableColumn
qtechWlogNotifyApRadioErrFrame=_QtechWlogNotifyApRadioErrFrame_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,5),_QtechWlogNotifyApRadioErrFrame_Type())
qtechWlogNotifyApRadioErrFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioErrFrame.setStatus(_B)
_QtechWlogNotifyApRadioRetrsmit_Type=Integer32
_QtechWlogNotifyApRadioRetrsmit_Object=MibTableColumn
qtechWlogNotifyApRadioRetrsmit=_QtechWlogNotifyApRadioRetrsmit_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,6),_QtechWlogNotifyApRadioRetrsmit_Type())
qtechWlogNotifyApRadioRetrsmit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioRetrsmit.setStatus(_B)
_QtechWlogNotifyApRadioTotalStaNum_Type=Integer32
_QtechWlogNotifyApRadioTotalStaNum_Object=MibTableColumn
qtechWlogNotifyApRadioTotalStaNum=_QtechWlogNotifyApRadioTotalStaNum_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,7),_QtechWlogNotifyApRadioTotalStaNum_Type())
qtechWlogNotifyApRadioTotalStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioTotalStaNum.setStatus(_B)
_QtechWlogNotifyApRadioWebStaNum_Type=Integer32
_QtechWlogNotifyApRadioWebStaNum_Object=MibTableColumn
qtechWlogNotifyApRadioWebStaNum=_QtechWlogNotifyApRadioWebStaNum_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,8),_QtechWlogNotifyApRadioWebStaNum_Type())
qtechWlogNotifyApRadioWebStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioWebStaNum.setStatus(_B)
_QtechWlogNotifyApRadioD1xStaNum_Type=Integer32
_QtechWlogNotifyApRadioD1xStaNum_Object=MibTableColumn
qtechWlogNotifyApRadioD1xStaNum=_QtechWlogNotifyApRadioD1xStaNum_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,7,1,9),_QtechWlogNotifyApRadioD1xStaNum_Type())
qtechWlogNotifyApRadioD1xStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyApRadioD1xStaNum.setStatus(_B)
_QtechWlogNotifyStaMac_Type=MacAddress
_QtechWlogNotifyStaMac_Object=MibScalar
qtechWlogNotifyStaMac=_QtechWlogNotifyStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,8),_QtechWlogNotifyStaMac_Type())
qtechWlogNotifyStaMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaMac.setStatus(_B)
_QtechWlogNotifyStaIp_Type=IpAddress
_QtechWlogNotifyStaIp_Object=MibScalar
qtechWlogNotifyStaIp=_QtechWlogNotifyStaIp_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,9),_QtechWlogNotifyStaIp_Type())
qtechWlogNotifyStaIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaIp.setStatus(_B)
_QtechWlogNotifyStaIpv6_Type=InetAddress
_QtechWlogNotifyStaIpv6_Object=MibScalar
qtechWlogNotifyStaIpv6=_QtechWlogNotifyStaIpv6_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,10),_QtechWlogNotifyStaIpv6_Type())
qtechWlogNotifyStaIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaIpv6.setStatus(_B)
_QtechWlogNotifySsid_Type=DisplayString
_QtechWlogNotifySsid_Object=MibScalar
qtechWlogNotifySsid=_QtechWlogNotifySsid_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,11),_QtechWlogNotifySsid_Type())
qtechWlogNotifySsid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifySsid.setStatus(_B)
_QtechWlogNotifyStaRssi_Type=Integer32
_QtechWlogNotifyStaRssi_Object=MibScalar
qtechWlogNotifyStaRssi=_QtechWlogNotifyStaRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,12),_QtechWlogNotifyStaRssi_Type())
qtechWlogNotifyStaRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaRssi.setStatus(_B)
_QtechWlogNotifyStaLinkrate_Type=Integer32
_QtechWlogNotifyStaLinkrate_Object=MibScalar
qtechWlogNotifyStaLinkrate=_QtechWlogNotifyStaLinkrate_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,13),_QtechWlogNotifyStaLinkrate_Type())
qtechWlogNotifyStaLinkrate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaLinkrate.setStatus(_B)
_QtechWlogNotifyStaOperType_Type=Integer32
_QtechWlogNotifyStaOperType_Object=MibScalar
qtechWlogNotifyStaOperType=_QtechWlogNotifyStaOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,14),_QtechWlogNotifyStaOperType_Type())
qtechWlogNotifyStaOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaOperType.setStatus(_B)
_QtechWlogNotifyStaAbnormalOperType_Type=Integer32
_QtechWlogNotifyStaAbnormalOperType_Object=MibScalar
qtechWlogNotifyStaAbnormalOperType=_QtechWlogNotifyStaAbnormalOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,15),_QtechWlogNotifyStaAbnormalOperType_Type())
qtechWlogNotifyStaAbnormalOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaAbnormalOperType.setStatus(_B)
_QtechWlogNotifyStaOperReason_Type=DisplayString
_QtechWlogNotifyStaOperReason_Object=MibScalar
qtechWlogNotifyStaOperReason=_QtechWlogNotifyStaOperReason_Object((1,3,6,1,4,1,27514,1,1,10,2,118,1,1,16),_QtechWlogNotifyStaOperReason_Type())
qtechWlogNotifyStaOperReason.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlogNotifyStaOperReason.setStatus(_B)
_QtechWlanWlogNotifications_ObjectIdentity=ObjectIdentity
qtechWlanWlogNotifications=_QtechWlanWlogNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,118,1,2))
qtechNotifyApCapwapDownReason=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,118,1,2,1))
qtechNotifyApCapwapDownReason.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_M)))
if mibBuilder.loadTexts:qtechNotifyApCapwapDownReason.setStatus(_B)
qtechNotifyApCapwapDownIntf=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,118,1,2,2))
qtechNotifyApCapwapDownIntf.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:qtechNotifyApCapwapDownIntf.setStatus(_B)
qtechNotifyApCapwapDownRadio=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,118,1,2,3))
qtechNotifyApCapwapDownRadio.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:qtechNotifyApCapwapDownRadio.setStatus(_B)
qtechNotifyStaOper=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,118,1,2,4))
qtechNotifyStaOper.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_f),(_A,_g),(_A,_D),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:qtechNotifyStaOper.setStatus(_B)
qtechNotifyStaAbnormalOper=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,118,1,2,5))
qtechNotifyStaAbnormalOper.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:qtechNotifyStaAbnormalOper.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechWlanWlogMIB':qtechWlanWlogMIB,'qtechWlanWlogNotificationsMIBObjects':qtechWlanWlogNotificationsMIBObjects,'qtechWlanWlogNtfObjects':qtechWlanWlogNtfObjects,_D:qtechWlogNotifyApName,_E:qtechWlogNotifyApMac,_F:qtechWlogNotifyApIp,_G:qtechWlogNotifyApCwDownId,_M:qtechWlogNotifyApCwDownReason,'qtechWlogNotifyApIntfStatTable':qtechWlogNotifyApIntfStatTable,'qtechWlogNotifyApIntfStatEntry':qtechWlogNotifyApIntfStatEntry,_H:qtechWlogNotifyApIntfName,_N:qtechWlogNotifyApIntfInputRate,_O:qtechWlogNotifyApIntfOutputRate,_P:qtechWlogNotifyApIntfUnicastInputPkts,_Q:qtechWlogNotifyApIntfUnicastOutputPkts,_R:qtechWlogNotifyApIntfMulticastInputPkts,_S:qtechWlogNotifyApIntfMulticastOutputPkts,_T:qtechWlogNotifyApIntfBroadcastInputPkts,_U:qtechWlogNotifyApIntfBroadcastOutputPkts,_V:qtechWlogNotifyApIntfErrorInputPkts,_W:qtechWlogNotifyApIntfErrorOutputPkts,'qtechWlogNotifyApRadioStatTable':qtechWlogNotifyApRadioStatTable,'qtechWlogNotifyApRadioStatEntry':qtechWlogNotifyApRadioStatEntry,_I:qtechWlogNotifyApRadioId,_X:qtechWlogNotifyApRadioWorkChnl,_Y:qtechWlogNotifyApRadioPower,_Z:qtechWlogNotifyApRadioRssi,_a:qtechWlogNotifyApRadioErrFrame,_b:qtechWlogNotifyApRadioRetrsmit,_c:qtechWlogNotifyApRadioTotalStaNum,_d:qtechWlogNotifyApRadioWebStaNum,_e:qtechWlogNotifyApRadioD1xStaNum,_J:qtechWlogNotifyStaMac,_K:qtechWlogNotifyStaIp,_L:qtechWlogNotifyStaIpv6,_h:qtechWlogNotifySsid,_f:qtechWlogNotifyStaRssi,_g:qtechWlogNotifyStaLinkrate,_i:qtechWlogNotifyStaOperType,_j:qtechWlogNotifyStaAbnormalOperType,_k:qtechWlogNotifyStaOperReason,'qtechWlanWlogNotifications':qtechWlanWlogNotifications,'qtechNotifyApCapwapDownReason':qtechNotifyApCapwapDownReason,'qtechNotifyApCapwapDownIntf':qtechNotifyApCapwapDownIntf,'qtechNotifyApCapwapDownRadio':qtechNotifyApCapwapDownRadio,'qtechNotifyStaOper':qtechNotifyStaOper,'qtechNotifyStaAbnormalOper':qtechNotifyStaAbnormalOper})