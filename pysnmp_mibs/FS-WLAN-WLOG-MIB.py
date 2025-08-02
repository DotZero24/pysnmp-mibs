_k='fsWlogNotifyStaOperReason'
_j='fsWlogNotifyStaAbnormalOperType'
_i='fsWlogNotifyStaOperType'
_h='fsWlogNotifySsid'
_g='fsWlogNotifyStaLinkrate'
_f='fsWlogNotifyStaRssi'
_e='fsWlogNotifyApRadioD1xStaNum'
_d='fsWlogNotifyApRadioWebStaNum'
_c='fsWlogNotifyApRadioTotalStaNum'
_b='fsWlogNotifyApRadioRetrsmit'
_a='fsWlogNotifyApRadioErrFrame'
_Z='fsWlogNotifyApRadioRssi'
_Y='fsWlogNotifyApRadioPower'
_X='fsWlogNotifyApRadioWorkChnl'
_W='fsWlogNotifyApIntfErrorOutputPkts'
_V='fsWlogNotifyApIntfErrorInputPkts'
_U='fsWlogNotifyApIntfBroadcastOutputPkts'
_T='fsWlogNotifyApIntfBroadcastInputPkts'
_S='fsWlogNotifyApIntfMulticastOutputPkts'
_R='fsWlogNotifyApIntfMulticastInputPkts'
_Q='fsWlogNotifyApIntfUnicastOutputPkts'
_P='fsWlogNotifyApIntfUnicastInputPkts'
_O='fsWlogNotifyApIntfOutputRate'
_N='fsWlogNotifyApIntfInputRate'
_M='fsWlogNotifyApCwDownReason'
_L='fsWlogNotifyStaIpv6'
_K='fsWlogNotifyStaIp'
_J='fsWlogNotifyStaMac'
_I='fsWlogNotifyApRadioId'
_H='fsWlogNotifyApIntfName'
_G='fsWlogNotifyApCwDownId'
_F='fsWlogNotifyApIp'
_E='fsWlogNotifyApMac'
_D='fsWlogNotifyApName'
_C='accessible-for-notify'
_B='current'
_A='FS-WLAN-WLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsWlanWlogMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,118))
if mibBuilder.loadTexts:fsWlanWlogMIB.setRevisions(('2012-10-10 00:00',))
_FsWlanWlogNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
fsWlanWlogNotificationsMIBObjects=_FsWlanWlogNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,118,1))
_FsWlanWlogNtfObjects_ObjectIdentity=ObjectIdentity
fsWlanWlogNtfObjects=_FsWlanWlogNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,118,1,1))
_FsWlogNotifyApName_Type=DisplayString
_FsWlogNotifyApName_Object=MibScalar
fsWlogNotifyApName=_FsWlogNotifyApName_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,1),_FsWlogNotifyApName_Type())
fsWlogNotifyApName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApName.setStatus(_B)
_FsWlogNotifyApMac_Type=MacAddress
_FsWlogNotifyApMac_Object=MibScalar
fsWlogNotifyApMac=_FsWlogNotifyApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,2),_FsWlogNotifyApMac_Type())
fsWlogNotifyApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApMac.setStatus(_B)
_FsWlogNotifyApIp_Type=InetAddress
_FsWlogNotifyApIp_Object=MibScalar
fsWlogNotifyApIp=_FsWlogNotifyApIp_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,3),_FsWlogNotifyApIp_Type())
fsWlogNotifyApIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIp.setStatus(_B)
_FsWlogNotifyApCwDownId_Type=Integer32
_FsWlogNotifyApCwDownId_Object=MibScalar
fsWlogNotifyApCwDownId=_FsWlogNotifyApCwDownId_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,4),_FsWlogNotifyApCwDownId_Type())
fsWlogNotifyApCwDownId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApCwDownId.setStatus(_B)
_FsWlogNotifyApCwDownReason_Type=DisplayString
_FsWlogNotifyApCwDownReason_Object=MibScalar
fsWlogNotifyApCwDownReason=_FsWlogNotifyApCwDownReason_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,5),_FsWlogNotifyApCwDownReason_Type())
fsWlogNotifyApCwDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApCwDownReason.setStatus(_B)
_FsWlogNotifyApIntfStatTable_Object=MibTable
fsWlogNotifyApIntfStatTable=_FsWlogNotifyApIntfStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6))
if mibBuilder.loadTexts:fsWlogNotifyApIntfStatTable.setStatus(_B)
_FsWlogNotifyApIntfStatEntry_Object=MibTableRow
fsWlogNotifyApIntfStatEntry=_FsWlogNotifyApIntfStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1))
fsWlogNotifyApIntfStatEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:fsWlogNotifyApIntfStatEntry.setStatus(_B)
_FsWlogNotifyApIntfName_Type=DisplayString
_FsWlogNotifyApIntfName_Object=MibTableColumn
fsWlogNotifyApIntfName=_FsWlogNotifyApIntfName_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,1),_FsWlogNotifyApIntfName_Type())
fsWlogNotifyApIntfName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfName.setStatus(_B)
_FsWlogNotifyApIntfInputRate_Type=Integer32
_FsWlogNotifyApIntfInputRate_Object=MibTableColumn
fsWlogNotifyApIntfInputRate=_FsWlogNotifyApIntfInputRate_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,2),_FsWlogNotifyApIntfInputRate_Type())
fsWlogNotifyApIntfInputRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfInputRate.setStatus(_B)
_FsWlogNotifyApIntfOutputRate_Type=Integer32
_FsWlogNotifyApIntfOutputRate_Object=MibTableColumn
fsWlogNotifyApIntfOutputRate=_FsWlogNotifyApIntfOutputRate_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,3),_FsWlogNotifyApIntfOutputRate_Type())
fsWlogNotifyApIntfOutputRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfOutputRate.setStatus(_B)
_FsWlogNotifyApIntfUnicastInputPkts_Type=Integer32
_FsWlogNotifyApIntfUnicastInputPkts_Object=MibTableColumn
fsWlogNotifyApIntfUnicastInputPkts=_FsWlogNotifyApIntfUnicastInputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,4),_FsWlogNotifyApIntfUnicastInputPkts_Type())
fsWlogNotifyApIntfUnicastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfUnicastInputPkts.setStatus(_B)
_FsWlogNotifyApIntfUnicastOutputPkts_Type=Integer32
_FsWlogNotifyApIntfUnicastOutputPkts_Object=MibTableColumn
fsWlogNotifyApIntfUnicastOutputPkts=_FsWlogNotifyApIntfUnicastOutputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,5),_FsWlogNotifyApIntfUnicastOutputPkts_Type())
fsWlogNotifyApIntfUnicastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfUnicastOutputPkts.setStatus(_B)
_FsWlogNotifyApIntfMulticastInputPkts_Type=Integer32
_FsWlogNotifyApIntfMulticastInputPkts_Object=MibTableColumn
fsWlogNotifyApIntfMulticastInputPkts=_FsWlogNotifyApIntfMulticastInputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,6),_FsWlogNotifyApIntfMulticastInputPkts_Type())
fsWlogNotifyApIntfMulticastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfMulticastInputPkts.setStatus(_B)
_FsWlogNotifyApIntfMulticastOutputPkts_Type=Integer32
_FsWlogNotifyApIntfMulticastOutputPkts_Object=MibTableColumn
fsWlogNotifyApIntfMulticastOutputPkts=_FsWlogNotifyApIntfMulticastOutputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,7),_FsWlogNotifyApIntfMulticastOutputPkts_Type())
fsWlogNotifyApIntfMulticastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfMulticastOutputPkts.setStatus(_B)
_FsWlogNotifyApIntfBroadcastInputPkts_Type=Integer32
_FsWlogNotifyApIntfBroadcastInputPkts_Object=MibTableColumn
fsWlogNotifyApIntfBroadcastInputPkts=_FsWlogNotifyApIntfBroadcastInputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,8),_FsWlogNotifyApIntfBroadcastInputPkts_Type())
fsWlogNotifyApIntfBroadcastInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfBroadcastInputPkts.setStatus(_B)
_FsWlogNotifyApIntfBroadcastOutputPkts_Type=Integer32
_FsWlogNotifyApIntfBroadcastOutputPkts_Object=MibTableColumn
fsWlogNotifyApIntfBroadcastOutputPkts=_FsWlogNotifyApIntfBroadcastOutputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,9),_FsWlogNotifyApIntfBroadcastOutputPkts_Type())
fsWlogNotifyApIntfBroadcastOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfBroadcastOutputPkts.setStatus(_B)
_FsWlogNotifyApIntfErrorInputPkts_Type=Integer32
_FsWlogNotifyApIntfErrorInputPkts_Object=MibTableColumn
fsWlogNotifyApIntfErrorInputPkts=_FsWlogNotifyApIntfErrorInputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,10),_FsWlogNotifyApIntfErrorInputPkts_Type())
fsWlogNotifyApIntfErrorInputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfErrorInputPkts.setStatus(_B)
_FsWlogNotifyApIntfErrorOutputPkts_Type=Integer32
_FsWlogNotifyApIntfErrorOutputPkts_Object=MibTableColumn
fsWlogNotifyApIntfErrorOutputPkts=_FsWlogNotifyApIntfErrorOutputPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,6,1,11),_FsWlogNotifyApIntfErrorOutputPkts_Type())
fsWlogNotifyApIntfErrorOutputPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApIntfErrorOutputPkts.setStatus(_B)
_FsWlogNotifyApRadioStatTable_Object=MibTable
fsWlogNotifyApRadioStatTable=_FsWlogNotifyApRadioStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7))
if mibBuilder.loadTexts:fsWlogNotifyApRadioStatTable.setStatus(_B)
_FsWlogNotifyApRadioStatEntry_Object=MibTableRow
fsWlogNotifyApRadioStatEntry=_FsWlogNotifyApRadioStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1))
fsWlogNotifyApRadioStatEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:fsWlogNotifyApRadioStatEntry.setStatus(_B)
_FsWlogNotifyApRadioId_Type=Integer32
_FsWlogNotifyApRadioId_Object=MibTableColumn
fsWlogNotifyApRadioId=_FsWlogNotifyApRadioId_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,1),_FsWlogNotifyApRadioId_Type())
fsWlogNotifyApRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioId.setStatus(_B)
_FsWlogNotifyApRadioWorkChnl_Type=Integer32
_FsWlogNotifyApRadioWorkChnl_Object=MibTableColumn
fsWlogNotifyApRadioWorkChnl=_FsWlogNotifyApRadioWorkChnl_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,2),_FsWlogNotifyApRadioWorkChnl_Type())
fsWlogNotifyApRadioWorkChnl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioWorkChnl.setStatus(_B)
_FsWlogNotifyApRadioPower_Type=Integer32
_FsWlogNotifyApRadioPower_Object=MibTableColumn
fsWlogNotifyApRadioPower=_FsWlogNotifyApRadioPower_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,3),_FsWlogNotifyApRadioPower_Type())
fsWlogNotifyApRadioPower.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioPower.setStatus(_B)
_FsWlogNotifyApRadioRssi_Type=Integer32
_FsWlogNotifyApRadioRssi_Object=MibTableColumn
fsWlogNotifyApRadioRssi=_FsWlogNotifyApRadioRssi_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,4),_FsWlogNotifyApRadioRssi_Type())
fsWlogNotifyApRadioRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioRssi.setStatus(_B)
_FsWlogNotifyApRadioErrFrame_Type=Integer32
_FsWlogNotifyApRadioErrFrame_Object=MibTableColumn
fsWlogNotifyApRadioErrFrame=_FsWlogNotifyApRadioErrFrame_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,5),_FsWlogNotifyApRadioErrFrame_Type())
fsWlogNotifyApRadioErrFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioErrFrame.setStatus(_B)
_FsWlogNotifyApRadioRetrsmit_Type=Integer32
_FsWlogNotifyApRadioRetrsmit_Object=MibTableColumn
fsWlogNotifyApRadioRetrsmit=_FsWlogNotifyApRadioRetrsmit_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,6),_FsWlogNotifyApRadioRetrsmit_Type())
fsWlogNotifyApRadioRetrsmit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioRetrsmit.setStatus(_B)
_FsWlogNotifyApRadioTotalStaNum_Type=Integer32
_FsWlogNotifyApRadioTotalStaNum_Object=MibTableColumn
fsWlogNotifyApRadioTotalStaNum=_FsWlogNotifyApRadioTotalStaNum_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,7),_FsWlogNotifyApRadioTotalStaNum_Type())
fsWlogNotifyApRadioTotalStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioTotalStaNum.setStatus(_B)
_FsWlogNotifyApRadioWebStaNum_Type=Integer32
_FsWlogNotifyApRadioWebStaNum_Object=MibTableColumn
fsWlogNotifyApRadioWebStaNum=_FsWlogNotifyApRadioWebStaNum_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,8),_FsWlogNotifyApRadioWebStaNum_Type())
fsWlogNotifyApRadioWebStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioWebStaNum.setStatus(_B)
_FsWlogNotifyApRadioD1xStaNum_Type=Integer32
_FsWlogNotifyApRadioD1xStaNum_Object=MibTableColumn
fsWlogNotifyApRadioD1xStaNum=_FsWlogNotifyApRadioD1xStaNum_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,7,1,9),_FsWlogNotifyApRadioD1xStaNum_Type())
fsWlogNotifyApRadioD1xStaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyApRadioD1xStaNum.setStatus(_B)
_FsWlogNotifyStaMac_Type=MacAddress
_FsWlogNotifyStaMac_Object=MibScalar
fsWlogNotifyStaMac=_FsWlogNotifyStaMac_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,8),_FsWlogNotifyStaMac_Type())
fsWlogNotifyStaMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaMac.setStatus(_B)
_FsWlogNotifyStaIp_Type=IpAddress
_FsWlogNotifyStaIp_Object=MibScalar
fsWlogNotifyStaIp=_FsWlogNotifyStaIp_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,9),_FsWlogNotifyStaIp_Type())
fsWlogNotifyStaIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaIp.setStatus(_B)
_FsWlogNotifyStaIpv6_Type=InetAddress
_FsWlogNotifyStaIpv6_Object=MibScalar
fsWlogNotifyStaIpv6=_FsWlogNotifyStaIpv6_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,10),_FsWlogNotifyStaIpv6_Type())
fsWlogNotifyStaIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaIpv6.setStatus(_B)
_FsWlogNotifySsid_Type=DisplayString
_FsWlogNotifySsid_Object=MibScalar
fsWlogNotifySsid=_FsWlogNotifySsid_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,11),_FsWlogNotifySsid_Type())
fsWlogNotifySsid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifySsid.setStatus(_B)
_FsWlogNotifyStaRssi_Type=Integer32
_FsWlogNotifyStaRssi_Object=MibScalar
fsWlogNotifyStaRssi=_FsWlogNotifyStaRssi_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,12),_FsWlogNotifyStaRssi_Type())
fsWlogNotifyStaRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaRssi.setStatus(_B)
_FsWlogNotifyStaLinkrate_Type=Integer32
_FsWlogNotifyStaLinkrate_Object=MibScalar
fsWlogNotifyStaLinkrate=_FsWlogNotifyStaLinkrate_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,13),_FsWlogNotifyStaLinkrate_Type())
fsWlogNotifyStaLinkrate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaLinkrate.setStatus(_B)
_FsWlogNotifyStaOperType_Type=Integer32
_FsWlogNotifyStaOperType_Object=MibScalar
fsWlogNotifyStaOperType=_FsWlogNotifyStaOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,14),_FsWlogNotifyStaOperType_Type())
fsWlogNotifyStaOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaOperType.setStatus(_B)
_FsWlogNotifyStaAbnormalOperType_Type=Integer32
_FsWlogNotifyStaAbnormalOperType_Object=MibScalar
fsWlogNotifyStaAbnormalOperType=_FsWlogNotifyStaAbnormalOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,15),_FsWlogNotifyStaAbnormalOperType_Type())
fsWlogNotifyStaAbnormalOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaAbnormalOperType.setStatus(_B)
_FsWlogNotifyStaOperReason_Type=DisplayString
_FsWlogNotifyStaOperReason_Object=MibScalar
fsWlogNotifyStaOperReason=_FsWlogNotifyStaOperReason_Object((1,3,6,1,4,1,52642,1,1,10,2,118,1,1,16),_FsWlogNotifyStaOperReason_Type())
fsWlogNotifyStaOperReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWlogNotifyStaOperReason.setStatus(_B)
_FsWlanWlogNotifications_ObjectIdentity=ObjectIdentity
fsWlanWlogNotifications=_FsWlanWlogNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,118,1,2))
fsNotifyApCapwapDownReason=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,118,1,2,1))
fsNotifyApCapwapDownReason.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_M)))
if mibBuilder.loadTexts:fsNotifyApCapwapDownReason.setStatus(_B)
fsNotifyApCapwapDownIntf=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,118,1,2,2))
fsNotifyApCapwapDownIntf.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:fsNotifyApCapwapDownIntf.setStatus(_B)
fsNotifyApCapwapDownRadio=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,118,1,2,3))
fsNotifyApCapwapDownRadio.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:fsNotifyApCapwapDownRadio.setStatus(_B)
fsNotifyStaOper=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,118,1,2,4))
fsNotifyStaOper.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_f),(_A,_g),(_A,_D),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:fsNotifyStaOper.setStatus(_B)
fsNotifyStaAbnormalOper=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,118,1,2,5))
fsNotifyStaAbnormalOper.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:fsNotifyStaAbnormalOper.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsWlanWlogMIB':fsWlanWlogMIB,'fsWlanWlogNotificationsMIBObjects':fsWlanWlogNotificationsMIBObjects,'fsWlanWlogNtfObjects':fsWlanWlogNtfObjects,_D:fsWlogNotifyApName,_E:fsWlogNotifyApMac,_F:fsWlogNotifyApIp,_G:fsWlogNotifyApCwDownId,_M:fsWlogNotifyApCwDownReason,'fsWlogNotifyApIntfStatTable':fsWlogNotifyApIntfStatTable,'fsWlogNotifyApIntfStatEntry':fsWlogNotifyApIntfStatEntry,_H:fsWlogNotifyApIntfName,_N:fsWlogNotifyApIntfInputRate,_O:fsWlogNotifyApIntfOutputRate,_P:fsWlogNotifyApIntfUnicastInputPkts,_Q:fsWlogNotifyApIntfUnicastOutputPkts,_R:fsWlogNotifyApIntfMulticastInputPkts,_S:fsWlogNotifyApIntfMulticastOutputPkts,_T:fsWlogNotifyApIntfBroadcastInputPkts,_U:fsWlogNotifyApIntfBroadcastOutputPkts,_V:fsWlogNotifyApIntfErrorInputPkts,_W:fsWlogNotifyApIntfErrorOutputPkts,'fsWlogNotifyApRadioStatTable':fsWlogNotifyApRadioStatTable,'fsWlogNotifyApRadioStatEntry':fsWlogNotifyApRadioStatEntry,_I:fsWlogNotifyApRadioId,_X:fsWlogNotifyApRadioWorkChnl,_Y:fsWlogNotifyApRadioPower,_Z:fsWlogNotifyApRadioRssi,_a:fsWlogNotifyApRadioErrFrame,_b:fsWlogNotifyApRadioRetrsmit,_c:fsWlogNotifyApRadioTotalStaNum,_d:fsWlogNotifyApRadioWebStaNum,_e:fsWlogNotifyApRadioD1xStaNum,_J:fsWlogNotifyStaMac,_K:fsWlogNotifyStaIp,_L:fsWlogNotifyStaIpv6,_h:fsWlogNotifySsid,_f:fsWlogNotifyStaRssi,_g:fsWlogNotifyStaLinkrate,_i:fsWlogNotifyStaOperType,_j:fsWlogNotifyStaAbnormalOperType,_k:fsWlogNotifyStaOperReason,'fsWlanWlogNotifications':fsWlanWlogNotifications,'fsNotifyApCapwapDownReason':fsNotifyApCapwapDownReason,'fsNotifyApCapwapDownIntf':fsNotifyApCapwapDownIntf,'fsNotifyApCapwapDownRadio':fsNotifyApCapwapDownRadio,'fsNotifyStaOper':fsNotifyStaOper,'fsNotifyStaAbnormalOper':fsNotifyStaAbnormalOper})