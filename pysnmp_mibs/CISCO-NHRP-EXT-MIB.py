_A7='cneServerGroup'
_A6='cneClientGroup'
_A5='cneServerNotificationGroup'
_A4='cneClientNotificationGroup'
_A3='cneGeneralGroup'
_A2='cneGeneralNotificationGroup'
_A1='cneNotificationControlGroup'
_A0='cneNotifNextHopRegClientDown'
_z='cneNotifNextHopRegClientUp'
_y='cneNotifNextHopRegServerDown'
_x='cneNotifNextHopRegServerUp'
_w='cneNotifNextHopPeerDown'
_v='cneNotifNextHopPeerUp'
_u='cneNotifRateLimitExceeded'
_t='cneNotifEnable'
_s='cneServerStatRedirectTx'
_r='cneClientStatRedirectRx'
_q='cneServerStatExtEntry'
_p='cneClientStatExtEntry'
_o='read-only'
_n='accessible-for-notify'
_m='nhrpServerNhcInUse'
_l='nhrpClientRegUniqueness'
_k='nhrpClientNhsInUse'
_j='nhrpClientHoldTime'
_i='nhrpCacheType'
_h='ifName'
_g='ifIndex'
_f='nhrpServerNhcPrefixLength'
_e='nhrpServerNhcNbmaSubaddr'
_d='nhrpServerNhcNbmaAddrType'
_c='nhrpServerNhcNbmaAddr'
_b='nhrpServerNhcInternetworkAddrType'
_a='nhrpServerNhcInternetworkAddr'
_Z='nhrpServerNbmaSubaddr'
_Y='nhrpServerNbmaAddrType'
_X='nhrpServerNbmaAddr'
_W='nhrpServerInternetworkAddrType'
_V='nhrpServerInternetworkAddr'
_U='nhrpServerCacheUniqueness'
_T='nhrpClientNhsNbmaSubaddr'
_S='nhrpClientNhsNbmaAddrType'
_R='nhrpClientNhsNbmaAddr'
_Q='nhrpClientNhsInternetworkAddrType'
_P='nhrpClientNhsInternetworkAddr'
_O='nhrpCacheNextHopInternetworkAddr'
_N='nhrpCacheNbmaSubaddr'
_M='nhrpCacheNbmaAddrType'
_L='nhrpCacheNbmaAddr'
_K='IF-MIB'
_J='cneNextHopDownReason'
_I='cneNHRPException'
_H='nhrpClientNbmaSubaddr'
_G='nhrpClientNbmaAddrType'
_F='nhrpClientNbmaAddr'
_E='nhrpClientInternetworkAddrType'
_D='nhrpClientInternetworkAddr'
_C='current'
_B='CISCO-NHRP-EXT-MIB'
_A='NHRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_K,_g,_h)
nhrpCacheNbmaAddr,nhrpCacheNbmaAddrType,nhrpCacheNbmaSubaddr,nhrpCacheNextHopInternetworkAddr,nhrpCacheType,nhrpClientHoldTime,nhrpClientIndex,nhrpClientInternetworkAddr,nhrpClientInternetworkAddrType,nhrpClientNbmaAddr,nhrpClientNbmaAddrType,nhrpClientNbmaSubaddr,nhrpClientNhsInUse,nhrpClientNhsInternetworkAddr,nhrpClientNhsInternetworkAddrType,nhrpClientNhsNbmaAddr,nhrpClientNhsNbmaAddrType,nhrpClientNhsNbmaSubaddr,nhrpClientRegUniqueness,nhrpClientStatEntry,nhrpServerCacheUniqueness,nhrpServerIndex,nhrpServerInternetworkAddr,nhrpServerInternetworkAddrType,nhrpServerNbmaAddr,nhrpServerNbmaAddrType,nhrpServerNbmaSubaddr,nhrpServerNhcInUse,nhrpServerNhcInternetworkAddr,nhrpServerNhcInternetworkAddrType,nhrpServerNhcNbmaAddr,nhrpServerNhcNbmaAddrType,nhrpServerNhcNbmaSubaddr,nhrpServerNhcPrefixLength,nhrpServerStatEntry=mibBuilder.importSymbols(_A,_L,_M,_N,_O,_i,_j,'nhrpClientIndex',_D,_E,_F,_G,_H,_k,_P,_Q,_R,_S,_T,_l,'nhrpClientStatEntry',_U,'nhrpServerIndex',_V,_W,_X,_Y,_Z,_m,_a,_b,_c,_d,_e,_f,'nhrpServerStatEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoNhrpExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,680))
if mibBuilder.loadTexts:ciscoNhrpExtMIB.setRevisions(('2008-11-21 00:00',))
class CiscoNhrpErrorCode(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,10,11,12,13,14,15,256)));namedValues=NamedValues(*(('unrecogExtension',1),('loopDetected',3),('adminProhibited',4),('insufficientResources',5),('addressUnreachable',6),('protocolError',7),('sduSizeExceeded',8),('invalidExtension',9),('invalidResReply',10),('authFailure',11),('noAddressBinding',12),('bindingNotUnique',13),('uniqueInternetworkAddrRegd',14),('hopCountExceeded',15),('other',256)))
class CiscoNextHopDownReasonCode(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('administrative',1),('registrationFailure',2),('resolutionFailure',3),('purgeReceived',4),('normalExpiry',5),('external',6),('other',7)))
_CneNotifs_ObjectIdentity=ObjectIdentity
cneNotifs=_CneNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,680,0))
_CneObjects_ObjectIdentity=ObjectIdentity
cneObjects=_CneObjects_ObjectIdentity((1,3,6,1,4,1,9,9,680,1))
_CneGeneralObjects_ObjectIdentity=ObjectIdentity
cneGeneralObjects=_CneGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9,9,680,1,1))
_CneNextHopDownReason_Type=CiscoNextHopDownReasonCode
_CneNextHopDownReason_Object=MibScalar
cneNextHopDownReason=_CneNextHopDownReason_Object((1,3,6,1,4,1,9,9,680,1,1,1),_CneNextHopDownReason_Type())
cneNextHopDownReason.setMaxAccess(_n)
if mibBuilder.loadTexts:cneNextHopDownReason.setStatus(_C)
_CneNHRPException_Type=CiscoNhrpErrorCode
_CneNHRPException_Object=MibScalar
cneNHRPException=_CneNHRPException_Object((1,3,6,1,4,1,9,9,680,1,1,2),_CneNHRPException_Type())
cneNHRPException.setMaxAccess(_n)
if mibBuilder.loadTexts:cneNHRPException.setStatus(_C)
_CneClientObjects_ObjectIdentity=ObjectIdentity
cneClientObjects=_CneClientObjects_ObjectIdentity((1,3,6,1,4,1,9,9,680,1,2))
_CneClientStatExtTable_Object=MibTable
cneClientStatExtTable=_CneClientStatExtTable_Object((1,3,6,1,4,1,9,9,680,1,2,1))
if mibBuilder.loadTexts:cneClientStatExtTable.setStatus(_C)
_CneClientStatExtEntry_Object=MibTableRow
cneClientStatExtEntry=_CneClientStatExtEntry_Object((1,3,6,1,4,1,9,9,680,1,2,1,1))
if mibBuilder.loadTexts:cneClientStatExtEntry.setStatus(_C)
_CneClientStatRedirectRx_Type=Counter32
_CneClientStatRedirectRx_Object=MibTableColumn
cneClientStatRedirectRx=_CneClientStatRedirectRx_Object((1,3,6,1,4,1,9,9,680,1,2,1,1,1),_CneClientStatRedirectRx_Type())
cneClientStatRedirectRx.setMaxAccess(_o)
if mibBuilder.loadTexts:cneClientStatRedirectRx.setStatus(_C)
_CneServerObjects_ObjectIdentity=ObjectIdentity
cneServerObjects=_CneServerObjects_ObjectIdentity((1,3,6,1,4,1,9,9,680,1,3))
_CneServerStatExtTable_Object=MibTable
cneServerStatExtTable=_CneServerStatExtTable_Object((1,3,6,1,4,1,9,9,680,1,3,1))
if mibBuilder.loadTexts:cneServerStatExtTable.setStatus(_C)
_CneServerStatExtEntry_Object=MibTableRow
cneServerStatExtEntry=_CneServerStatExtEntry_Object((1,3,6,1,4,1,9,9,680,1,3,1,1))
if mibBuilder.loadTexts:cneServerStatExtEntry.setStatus(_C)
_CneServerStatRedirectTx_Type=Counter32
_CneServerStatRedirectTx_Object=MibTableColumn
cneServerStatRedirectTx=_CneServerStatRedirectTx_Object((1,3,6,1,4,1,9,9,680,1,3,1,1,1),_CneServerStatRedirectTx_Type())
cneServerStatRedirectTx.setMaxAccess(_o)
if mibBuilder.loadTexts:cneServerStatRedirectTx.setStatus(_C)
_CneNotificationControlObjects_ObjectIdentity=ObjectIdentity
cneNotificationControlObjects=_CneNotificationControlObjects_ObjectIdentity((1,3,6,1,4,1,9,9,680,1,4))
class _CneNotifEnable_Type(Bits):defaultBinValue='1111001';namedValues=NamedValues(*(('nextHopRegServerUp',0),('nextHopRegServerDown',1),('nextHopRegClientUp',2),('nextHopRegClientDown',3),('nextHopPeerUp',4),('nextHopPeerDown',5),('rateLimitExceeded',6)))
_CneNotifEnable_Type.__name__='Bits'
_CneNotifEnable_Object=MibScalar
cneNotifEnable=_CneNotifEnable_Object((1,3,6,1,4,1,9,9,680,1,4,1),_CneNotifEnable_Type())
cneNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cneNotifEnable.setStatus(_C)
_CneConform_ObjectIdentity=ObjectIdentity
cneConform=_CneConform_ObjectIdentity((1,3,6,1,4,1,9,9,680,2))
_CneCompliances_ObjectIdentity=ObjectIdentity
cneCompliances=_CneCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,680,2,1))
_CneGroups_ObjectIdentity=ObjectIdentity
cneGroups=_CneGroups_ObjectIdentity((1,3,6,1,4,1,9,9,680,2,2))
nhrpClientStatEntry.registerAugmentions((_B,_p))
cneClientStatExtEntry.setIndexNames(*nhrpClientStatEntry.getIndexNames())
nhrpServerStatEntry.registerAugmentions((_B,_q))
cneServerStatExtEntry.setIndexNames(*nhrpServerStatEntry.getIndexNames())
cneGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,680,2,2,1))
cneGeneralGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cneGeneralGroup.setStatus(_C)
cneClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,680,2,2,2))
cneClientGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:cneClientGroup.setStatus(_C)
cneServerGroup=ObjectGroup((1,3,6,1,4,1,9,9,680,2,2,3))
cneServerGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:cneServerGroup.setStatus(_C)
cneNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,680,2,2,4))
cneNotificationControlGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:cneNotificationControlGroup.setStatus(_C)
cneNotifNextHopRegServerUp=NotificationType((1,3,6,1,4,1,9,9,680,0,1))
cneNotifNextHopRegServerUp.setObjects(*((_A,_E),(_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_Q),(_A,_P),(_A,_S),(_A,_R),(_A,_T),(_A,_j),(_A,_l),(_A,_k)))
if mibBuilder.loadTexts:cneNotifNextHopRegServerUp.setStatus(_C)
cneNotifNextHopRegServerDown=NotificationType((1,3,6,1,4,1,9,9,680,0,2))
cneNotifNextHopRegServerDown.setObjects(*((_A,_E),(_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_Q),(_A,_P),(_A,_S),(_A,_R),(_A,_T),(_B,_J),(_B,_I)))
if mibBuilder.loadTexts:cneNotifNextHopRegServerDown.setStatus(_C)
cneNotifNextHopRegClientUp=NotificationType((1,3,6,1,4,1,9,9,680,0,3))
cneNotifNextHopRegClientUp.setObjects(*((_A,_W),(_A,_V),(_A,_Y),(_A,_X),(_A,_Z),(_A,_b),(_A,_a),(_A,_d),(_A,_c),(_A,_e),(_A,_f),(_A,_m),(_A,_U)))
if mibBuilder.loadTexts:cneNotifNextHopRegClientUp.setStatus(_C)
cneNotifNextHopRegClientDown=NotificationType((1,3,6,1,4,1,9,9,680,0,4))
cneNotifNextHopRegClientDown.setObjects(*((_A,_W),(_A,_V),(_A,_Y),(_A,_X),(_A,_Z),(_A,_b),(_A,_a),(_A,_d),(_A,_c),(_A,_e),(_A,_f),(_A,_U),(_B,_J),(_B,_I)))
if mibBuilder.loadTexts:cneNotifNextHopRegClientDown.setStatus(_C)
cneNotifNextHopPeerUp=NotificationType((1,3,6,1,4,1,9,9,680,0,5))
cneNotifNextHopPeerUp.setObjects(*((_A,_E),(_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_O),(_A,_M),(_A,_L),(_A,_N),(_A,_i)))
if mibBuilder.loadTexts:cneNotifNextHopPeerUp.setStatus(_C)
cneNotifNextHopPeerDown=NotificationType((1,3,6,1,4,1,9,9,680,0,6))
cneNotifNextHopPeerDown.setObjects(*((_A,_E),(_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_O),(_A,_M),(_A,_L),(_A,_N),(_B,_J),(_B,_I)))
if mibBuilder.loadTexts:cneNotifNextHopPeerDown.setStatus(_C)
cneNotifRateLimitExceeded=NotificationType((1,3,6,1,4,1,9,9,680,0,7))
cneNotifRateLimitExceeded.setObjects(*((_K,_g),(_K,_h)))
if mibBuilder.loadTexts:cneNotifRateLimitExceeded.setStatus(_C)
cneGeneralNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,680,2,2,5))
cneGeneralNotificationGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cneGeneralNotificationGroup.setStatus(_C)
cneClientNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,680,2,2,6))
cneClientNotificationGroup.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cneClientNotificationGroup.setStatus(_C)
cneServerNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,680,2,2,7))
cneServerNotificationGroup.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cneServerNotificationGroup.setStatus(_C)
cneCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,680,2,1,1))
cneCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:cneCompliance.setStatus(_C)
mibBuilder.exportSymbols(_B,**{'CiscoNhrpErrorCode':CiscoNhrpErrorCode,'CiscoNextHopDownReasonCode':CiscoNextHopDownReasonCode,'ciscoNhrpExtMIB':ciscoNhrpExtMIB,'cneNotifs':cneNotifs,_x:cneNotifNextHopRegServerUp,_y:cneNotifNextHopRegServerDown,_z:cneNotifNextHopRegClientUp,_A0:cneNotifNextHopRegClientDown,_v:cneNotifNextHopPeerUp,_w:cneNotifNextHopPeerDown,_u:cneNotifRateLimitExceeded,'cneObjects':cneObjects,'cneGeneralObjects':cneGeneralObjects,_J:cneNextHopDownReason,_I:cneNHRPException,'cneClientObjects':cneClientObjects,'cneClientStatExtTable':cneClientStatExtTable,_p:cneClientStatExtEntry,_r:cneClientStatRedirectRx,'cneServerObjects':cneServerObjects,'cneServerStatExtTable':cneServerStatExtTable,_q:cneServerStatExtEntry,_s:cneServerStatRedirectTx,'cneNotificationControlObjects':cneNotificationControlObjects,_t:cneNotifEnable,'cneConform':cneConform,'cneCompliances':cneCompliances,'cneCompliance':cneCompliance,'cneGroups':cneGroups,_A3:cneGeneralGroup,_A6:cneClientGroup,_A7:cneServerGroup,_A1:cneNotificationControlGroup,_A2:cneGeneralNotificationGroup,_A4:cneClientNotificationGroup,_A5:cneServerNotificationGroup})