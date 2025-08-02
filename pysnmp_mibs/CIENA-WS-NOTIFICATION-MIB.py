_A8='wsLinkStateAlarmNotificationEntityType'
_A7='wsLinkStateAlarmNotificationOduSkewOor'
_A6='wsLinkStateAlarmNotificationOduFeClientSf'
_A5='wsLinkStateAlarmNotificationOduPtiMismatch'
_A4='wsLinkStateAlarmNotificationOduBdi'
_A3='wsLinkStateAlarmNotificationOduTtiMismatch'
_A2='wsLinkStateAlarmNotificationOduSd'
_A1='wsLinkStateAlarmNotificationOduSf'
_A0='wsLinkStateAlarmNotificationOduLck'
_z='wsLinkStateAlarmNotificationOduAis'
_y='wsLinkStateAlarmNotificationOduOci'
_x='wsLinkStateAlarmNotificationOtuTtiMismatch'
_w='wsLinkStateAlarmNotificationOtuBdi'
_v='wsLinkStateAlarmNotificationOtuLom'
_u='wsLinkStateAlarmNotificationOtuPreFecSd'
_t='wsLinkStateAlarmNotificationOtuPreFecSf'
_s='wsLinkStateAlarmNotificationOtuLof'
_r='wsLinkStateAlarmNotificationOtuFreqOor'
_q='wsLinkStateAlarmNotificationOtuLoc'
_p='wsLinkStateAlarmNotificationEthRsLinkDown'
_o='wsLinkStateAlarmNotificationEthPcsLoam'
_n='wsLinkStateAlarmNotificationEthPcsLobl'
_m='wsLinkStateAlarmNotificationEthRsRf'
_l='wsLinkStateAlarmNotificationEthRsLf'
_k='wsLinkStateAlarmNotificationEthFecLossSync'
_j='wsLinkStateAlarmNotificationPtpTxLol'
_i='wsLinkStateAlarmNotificationPtpTxLos'
_h='wsLinkStateAlarmNotificationPtpRxLol'
_g='wsLinkStateAlarmNotificationPtpRxLos'
_f='wsLinkStateAlarmNotificationDescription'
_e='wsLinkStateAlarmNotificationInstance'
_d='wsLinkStateAlarmNotificationSeverity'
_c='wsLinkStateAlarmNotificationDateAndTime'
_b='wsLinkStateAlarmNotificationInstanceId'
_a='wsLinkStateAlarmNotificationMemberId'
_Z='wsLinkStateAlarmNotificationGroupId'
_Y='wsLinkStateAlarmNotificationSiteId'
_X='wsAlarmNotificationEntityType'
_W='wsAlarmNotificationActiveStatus'
_V='wsAlarmNotificationDescription'
_U='wsAlarmNotificationInstance'
_T='wsAlarmNotificationSeverity'
_S='wsAlarmNotificationTableId'
_R='wsAlarmNotificationDateAndTime'
_Q='wsAlarmNotificationInstanceId'
_P='wsAlarmNotificationMemberId'
_O='wsAlarmNotificationGroupId'
_N='wsAlarmNotificationSiteId'
_M='linePort'
_L='clientPort'
_K='notApplicable'
_J='warning'
_I='critical'
_H='cleared'
_G='Unsigned32'
_F='inactive'
_E='active'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-NOTIFICATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsNotifications,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsNotifications')
StringMaxl44,=mibBuilder.importSymbols('CIENA-WS-PLATFORM-TYPEDEFS-MIB','StringMaxl44')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaWsNotificationMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,2,3))
if mibBuilder.loadTexts:cienaWsNotificationMIB.setRevisions(('2019-09-09 00:00','2018-01-15 00:00','2016-11-14 00:00'))
class DisplayString32(TextualConvention,OctetString):status=_A;displayHint='32t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WsAlarmNotificationSiteId_Type=Unsigned32
_WsAlarmNotificationSiteId_Object=MibScalar
wsAlarmNotificationSiteId=_WsAlarmNotificationSiteId_Object((1,3,6,1,4,1,1271,3,2,11,1),_WsAlarmNotificationSiteId_Type())
wsAlarmNotificationSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationSiteId.setStatus(_A)
_WsAlarmNotificationGroupId_Type=Unsigned32
_WsAlarmNotificationGroupId_Object=MibScalar
wsAlarmNotificationGroupId=_WsAlarmNotificationGroupId_Object((1,3,6,1,4,1,1271,3,2,11,2),_WsAlarmNotificationGroupId_Type())
wsAlarmNotificationGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationGroupId.setStatus(_A)
_WsAlarmNotificationMemberId_Type=Unsigned32
_WsAlarmNotificationMemberId_Object=MibScalar
wsAlarmNotificationMemberId=_WsAlarmNotificationMemberId_Object((1,3,6,1,4,1,1271,3,2,11,3),_WsAlarmNotificationMemberId_Type())
wsAlarmNotificationMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationMemberId.setStatus(_A)
class _WsAlarmNotificationInstanceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WsAlarmNotificationInstanceId_Type.__name__=_G
_WsAlarmNotificationInstanceId_Object=MibScalar
wsAlarmNotificationInstanceId=_WsAlarmNotificationInstanceId_Object((1,3,6,1,4,1,1271,3,2,11,4),_WsAlarmNotificationInstanceId_Type())
wsAlarmNotificationInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationInstanceId.setStatus(_A)
_WsAlarmNotificationDateAndTime_Type=DisplayString32
_WsAlarmNotificationDateAndTime_Object=MibScalar
wsAlarmNotificationDateAndTime=_WsAlarmNotificationDateAndTime_Object((1,3,6,1,4,1,1271,3,2,11,5),_WsAlarmNotificationDateAndTime_Type())
wsAlarmNotificationDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationDateAndTime.setStatus(_A)
_WsAlarmNotificationTableId_Type=Unsigned32
_WsAlarmNotificationTableId_Object=MibScalar
wsAlarmNotificationTableId=_WsAlarmNotificationTableId_Object((1,3,6,1,4,1,1271,3,2,11,6),_WsAlarmNotificationTableId_Type())
wsAlarmNotificationTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationTableId.setStatus(_A)
class _WsAlarmNotificationSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,8)));namedValues=NamedValues(*((_H,1),(_I,3),('major',4),('minor',5),(_J,6),('info',8)))
_WsAlarmNotificationSeverity_Type.__name__=_D
_WsAlarmNotificationSeverity_Object=MibScalar
wsAlarmNotificationSeverity=_WsAlarmNotificationSeverity_Object((1,3,6,1,4,1,1271,3,2,11,7),_WsAlarmNotificationSeverity_Type())
wsAlarmNotificationSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationSeverity.setStatus(_A)
_WsAlarmNotificationInstance_Type=DisplayString32
_WsAlarmNotificationInstance_Object=MibScalar
wsAlarmNotificationInstance=_WsAlarmNotificationInstance_Object((1,3,6,1,4,1,1271,3,2,11,8),_WsAlarmNotificationInstance_Type())
wsAlarmNotificationInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationInstance.setStatus(_A)
_WsAlarmNotificationDescription_Type=StringMaxl44
_WsAlarmNotificationDescription_Object=MibScalar
wsAlarmNotificationDescription=_WsAlarmNotificationDescription_Object((1,3,6,1,4,1,1271,3,2,11,9),_WsAlarmNotificationDescription_Type())
wsAlarmNotificationDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationDescription.setStatus(_A)
class _WsAlarmNotificationActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),('intermittent',3)))
_WsAlarmNotificationActiveStatus_Type.__name__=_D
_WsAlarmNotificationActiveStatus_Object=MibScalar
wsAlarmNotificationActiveStatus=_WsAlarmNotificationActiveStatus_Object((1,3,6,1,4,1,1271,3,2,11,10),_WsAlarmNotificationActiveStatus_Type())
wsAlarmNotificationActiveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationActiveStatus.setStatus(_A)
class _WsAlarmNotificationEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('other',1),(_L,2),(_M,3)))
_WsAlarmNotificationEntityType_Type.__name__=_D
_WsAlarmNotificationEntityType_Object=MibScalar
wsAlarmNotificationEntityType=_WsAlarmNotificationEntityType_Object((1,3,6,1,4,1,1271,3,2,11,11),_WsAlarmNotificationEntityType_Type())
wsAlarmNotificationEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:wsAlarmNotificationEntityType.setStatus(_A)
_WsLinkStateAlarmNotificationSiteId_Type=Unsigned32
_WsLinkStateAlarmNotificationSiteId_Object=MibScalar
wsLinkStateAlarmNotificationSiteId=_WsLinkStateAlarmNotificationSiteId_Object((1,3,6,1,4,1,1271,3,2,12,1),_WsLinkStateAlarmNotificationSiteId_Type())
wsLinkStateAlarmNotificationSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationSiteId.setStatus(_A)
_WsLinkStateAlarmNotificationGroupId_Type=Unsigned32
_WsLinkStateAlarmNotificationGroupId_Object=MibScalar
wsLinkStateAlarmNotificationGroupId=_WsLinkStateAlarmNotificationGroupId_Object((1,3,6,1,4,1,1271,3,2,12,2),_WsLinkStateAlarmNotificationGroupId_Type())
wsLinkStateAlarmNotificationGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationGroupId.setStatus(_A)
_WsLinkStateAlarmNotificationMemberId_Type=Unsigned32
_WsLinkStateAlarmNotificationMemberId_Object=MibScalar
wsLinkStateAlarmNotificationMemberId=_WsLinkStateAlarmNotificationMemberId_Object((1,3,6,1,4,1,1271,3,2,12,3),_WsLinkStateAlarmNotificationMemberId_Type())
wsLinkStateAlarmNotificationMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationMemberId.setStatus(_A)
class _WsLinkStateAlarmNotificationInstanceId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WsLinkStateAlarmNotificationInstanceId_Type.__name__=_G
_WsLinkStateAlarmNotificationInstanceId_Object=MibScalar
wsLinkStateAlarmNotificationInstanceId=_WsLinkStateAlarmNotificationInstanceId_Object((1,3,6,1,4,1,1271,3,2,12,4),_WsLinkStateAlarmNotificationInstanceId_Type())
wsLinkStateAlarmNotificationInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationInstanceId.setStatus(_A)
_WsLinkStateAlarmNotificationDateAndTime_Type=DisplayString32
_WsLinkStateAlarmNotificationDateAndTime_Object=MibScalar
wsLinkStateAlarmNotificationDateAndTime=_WsLinkStateAlarmNotificationDateAndTime_Object((1,3,6,1,4,1,1271,3,2,12,5),_WsLinkStateAlarmNotificationDateAndTime_Type())
wsLinkStateAlarmNotificationDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationDateAndTime.setStatus(_A)
class _WsLinkStateAlarmNotificationSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,8)));namedValues=NamedValues(*((_H,1),(_I,3),('major',4),('minor',5),(_J,6),('info',8)))
_WsLinkStateAlarmNotificationSeverity_Type.__name__=_D
_WsLinkStateAlarmNotificationSeverity_Object=MibScalar
wsLinkStateAlarmNotificationSeverity=_WsLinkStateAlarmNotificationSeverity_Object((1,3,6,1,4,1,1271,3,2,12,7),_WsLinkStateAlarmNotificationSeverity_Type())
wsLinkStateAlarmNotificationSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationSeverity.setStatus(_A)
_WsLinkStateAlarmNotificationInstance_Type=DisplayString32
_WsLinkStateAlarmNotificationInstance_Object=MibScalar
wsLinkStateAlarmNotificationInstance=_WsLinkStateAlarmNotificationInstance_Object((1,3,6,1,4,1,1271,3,2,12,8),_WsLinkStateAlarmNotificationInstance_Type())
wsLinkStateAlarmNotificationInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationInstance.setStatus(_A)
_WsLinkStateAlarmNotificationDescription_Type=DisplayString32
_WsLinkStateAlarmNotificationDescription_Object=MibScalar
wsLinkStateAlarmNotificationDescription=_WsLinkStateAlarmNotificationDescription_Object((1,3,6,1,4,1,1271,3,2,12,9),_WsLinkStateAlarmNotificationDescription_Type())
wsLinkStateAlarmNotificationDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationDescription.setStatus(_A)
_WsLinkStateAlarmNotificationPtpDefects_ObjectIdentity=ObjectIdentity
wsLinkStateAlarmNotificationPtpDefects=_WsLinkStateAlarmNotificationPtpDefects_ObjectIdentity((1,3,6,1,4,1,1271,3,2,12,10))
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationPtpDefects.setStatus(_A)
class _WsLinkStateAlarmNotificationPtpRxLos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationPtpRxLos_Type.__name__=_D
_WsLinkStateAlarmNotificationPtpRxLos_Object=MibScalar
wsLinkStateAlarmNotificationPtpRxLos=_WsLinkStateAlarmNotificationPtpRxLos_Object((1,3,6,1,4,1,1271,3,2,12,10,1),_WsLinkStateAlarmNotificationPtpRxLos_Type())
wsLinkStateAlarmNotificationPtpRxLos.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationPtpRxLos.setStatus(_A)
class _WsLinkStateAlarmNotificationPtpRxLol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationPtpRxLol_Type.__name__=_D
_WsLinkStateAlarmNotificationPtpRxLol_Object=MibScalar
wsLinkStateAlarmNotificationPtpRxLol=_WsLinkStateAlarmNotificationPtpRxLol_Object((1,3,6,1,4,1,1271,3,2,12,10,2),_WsLinkStateAlarmNotificationPtpRxLol_Type())
wsLinkStateAlarmNotificationPtpRxLol.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationPtpRxLol.setStatus(_A)
class _WsLinkStateAlarmNotificationPtpTxLos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationPtpTxLos_Type.__name__=_D
_WsLinkStateAlarmNotificationPtpTxLos_Object=MibScalar
wsLinkStateAlarmNotificationPtpTxLos=_WsLinkStateAlarmNotificationPtpTxLos_Object((1,3,6,1,4,1,1271,3,2,12,10,3),_WsLinkStateAlarmNotificationPtpTxLos_Type())
wsLinkStateAlarmNotificationPtpTxLos.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationPtpTxLos.setStatus(_A)
class _WsLinkStateAlarmNotificationPtpTxLol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationPtpTxLol_Type.__name__=_D
_WsLinkStateAlarmNotificationPtpTxLol_Object=MibScalar
wsLinkStateAlarmNotificationPtpTxLol=_WsLinkStateAlarmNotificationPtpTxLol_Object((1,3,6,1,4,1,1271,3,2,12,10,4),_WsLinkStateAlarmNotificationPtpTxLol_Type())
wsLinkStateAlarmNotificationPtpTxLol.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationPtpTxLol.setStatus(_A)
_WsLinkStateAlarmNotificationEthDefects_ObjectIdentity=ObjectIdentity
wsLinkStateAlarmNotificationEthDefects=_WsLinkStateAlarmNotificationEthDefects_ObjectIdentity((1,3,6,1,4,1,1271,3,2,12,11))
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthDefects.setStatus(_A)
class _WsLinkStateAlarmNotificationEthPcsHighBer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthPcsHighBer_Type.__name__=_D
_WsLinkStateAlarmNotificationEthPcsHighBer_Object=MibScalar
wsLinkStateAlarmNotificationEthPcsHighBer=_WsLinkStateAlarmNotificationEthPcsHighBer_Object((1,3,6,1,4,1,1271,3,2,12,11,1),_WsLinkStateAlarmNotificationEthPcsHighBer_Type())
wsLinkStateAlarmNotificationEthPcsHighBer.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthPcsHighBer.setStatus(_A)
class _WsLinkStateAlarmNotificationEthPcsLoam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthPcsLoam_Type.__name__=_D
_WsLinkStateAlarmNotificationEthPcsLoam_Object=MibScalar
wsLinkStateAlarmNotificationEthPcsLoam=_WsLinkStateAlarmNotificationEthPcsLoam_Object((1,3,6,1,4,1,1271,3,2,12,11,2),_WsLinkStateAlarmNotificationEthPcsLoam_Type())
wsLinkStateAlarmNotificationEthPcsLoam.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthPcsLoam.setStatus(_A)
class _WsLinkStateAlarmNotificationEthPcsLobl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthPcsLobl_Type.__name__=_D
_WsLinkStateAlarmNotificationEthPcsLobl_Object=MibScalar
wsLinkStateAlarmNotificationEthPcsLobl=_WsLinkStateAlarmNotificationEthPcsLobl_Object((1,3,6,1,4,1,1271,3,2,12,11,3),_WsLinkStateAlarmNotificationEthPcsLobl_Type())
wsLinkStateAlarmNotificationEthPcsLobl.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthPcsLobl.setStatus(_A)
class _WsLinkStateAlarmNotificationEthRsLinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthRsLinkDown_Type.__name__=_D
_WsLinkStateAlarmNotificationEthRsLinkDown_Object=MibScalar
wsLinkStateAlarmNotificationEthRsLinkDown=_WsLinkStateAlarmNotificationEthRsLinkDown_Object((1,3,6,1,4,1,1271,3,2,12,11,4),_WsLinkStateAlarmNotificationEthRsLinkDown_Type())
wsLinkStateAlarmNotificationEthRsLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthRsLinkDown.setStatus(_A)
class _WsLinkStateAlarmNotificationEthRsLf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthRsLf_Type.__name__=_D
_WsLinkStateAlarmNotificationEthRsLf_Object=MibScalar
wsLinkStateAlarmNotificationEthRsLf=_WsLinkStateAlarmNotificationEthRsLf_Object((1,3,6,1,4,1,1271,3,2,12,11,5),_WsLinkStateAlarmNotificationEthRsLf_Type())
wsLinkStateAlarmNotificationEthRsLf.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthRsLf.setStatus(_A)
class _WsLinkStateAlarmNotificationEthRsRf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthRsRf_Type.__name__=_D
_WsLinkStateAlarmNotificationEthRsRf_Object=MibScalar
wsLinkStateAlarmNotificationEthRsRf=_WsLinkStateAlarmNotificationEthRsRf_Object((1,3,6,1,4,1,1271,3,2,12,11,6),_WsLinkStateAlarmNotificationEthRsRf_Type())
wsLinkStateAlarmNotificationEthRsRf.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthRsRf.setStatus(_A)
class _WsLinkStateAlarmNotificationEthFecLossSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthFecLossSync_Type.__name__=_D
_WsLinkStateAlarmNotificationEthFecLossSync_Object=MibScalar
wsLinkStateAlarmNotificationEthFecLossSync=_WsLinkStateAlarmNotificationEthFecLossSync_Object((1,3,6,1,4,1,1271,3,2,12,11,7),_WsLinkStateAlarmNotificationEthFecLossSync_Type())
wsLinkStateAlarmNotificationEthFecLossSync.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthFecLossSync.setStatus(_A)
class _WsLinkStateAlarmNotificationEthPmaSool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationEthPmaSool_Type.__name__=_D
_WsLinkStateAlarmNotificationEthPmaSool_Object=MibScalar
wsLinkStateAlarmNotificationEthPmaSool=_WsLinkStateAlarmNotificationEthPmaSool_Object((1,3,6,1,4,1,1271,3,2,12,11,8),_WsLinkStateAlarmNotificationEthPmaSool_Type())
wsLinkStateAlarmNotificationEthPmaSool.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEthPmaSool.setStatus(_A)
_WsLinkStateAlarmNotificationOtuDefects_ObjectIdentity=ObjectIdentity
wsLinkStateAlarmNotificationOtuDefects=_WsLinkStateAlarmNotificationOtuDefects_ObjectIdentity((1,3,6,1,4,1,1271,3,2,12,12))
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuDefects.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuLoc_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuLoc_Object=MibScalar
wsLinkStateAlarmNotificationOtuLoc=_WsLinkStateAlarmNotificationOtuLoc_Object((1,3,6,1,4,1,1271,3,2,12,12,1),_WsLinkStateAlarmNotificationOtuLoc_Type())
wsLinkStateAlarmNotificationOtuLoc.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuLoc.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuFreqOor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuFreqOor_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuFreqOor_Object=MibScalar
wsLinkStateAlarmNotificationOtuFreqOor=_WsLinkStateAlarmNotificationOtuFreqOor_Object((1,3,6,1,4,1,1271,3,2,12,12,2),_WsLinkStateAlarmNotificationOtuFreqOor_Type())
wsLinkStateAlarmNotificationOtuFreqOor.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuFreqOor.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuLof_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuLof_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuLof_Object=MibScalar
wsLinkStateAlarmNotificationOtuLof=_WsLinkStateAlarmNotificationOtuLof_Object((1,3,6,1,4,1,1271,3,2,12,12,3),_WsLinkStateAlarmNotificationOtuLof_Type())
wsLinkStateAlarmNotificationOtuLof.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuLof.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuPreFecSf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuPreFecSf_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuPreFecSf_Object=MibScalar
wsLinkStateAlarmNotificationOtuPreFecSf=_WsLinkStateAlarmNotificationOtuPreFecSf_Object((1,3,6,1,4,1,1271,3,2,12,12,4),_WsLinkStateAlarmNotificationOtuPreFecSf_Type())
wsLinkStateAlarmNotificationOtuPreFecSf.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuPreFecSf.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuPreFecSd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuPreFecSd_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuPreFecSd_Object=MibScalar
wsLinkStateAlarmNotificationOtuPreFecSd=_WsLinkStateAlarmNotificationOtuPreFecSd_Object((1,3,6,1,4,1,1271,3,2,12,12,5),_WsLinkStateAlarmNotificationOtuPreFecSd_Type())
wsLinkStateAlarmNotificationOtuPreFecSd.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuPreFecSd.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuLom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuLom_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuLom_Object=MibScalar
wsLinkStateAlarmNotificationOtuLom=_WsLinkStateAlarmNotificationOtuLom_Object((1,3,6,1,4,1,1271,3,2,12,12,6),_WsLinkStateAlarmNotificationOtuLom_Type())
wsLinkStateAlarmNotificationOtuLom.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuLom.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuBdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuBdi_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuBdi_Object=MibScalar
wsLinkStateAlarmNotificationOtuBdi=_WsLinkStateAlarmNotificationOtuBdi_Object((1,3,6,1,4,1,1271,3,2,12,12,7),_WsLinkStateAlarmNotificationOtuBdi_Type())
wsLinkStateAlarmNotificationOtuBdi.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuBdi.setStatus(_A)
class _WsLinkStateAlarmNotificationOtuTtiMismatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOtuTtiMismatch_Type.__name__=_D
_WsLinkStateAlarmNotificationOtuTtiMismatch_Object=MibScalar
wsLinkStateAlarmNotificationOtuTtiMismatch=_WsLinkStateAlarmNotificationOtuTtiMismatch_Object((1,3,6,1,4,1,1271,3,2,12,12,8),_WsLinkStateAlarmNotificationOtuTtiMismatch_Type())
wsLinkStateAlarmNotificationOtuTtiMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOtuTtiMismatch.setStatus(_A)
_WsLinkStateAlarmNotificationOduDefects_ObjectIdentity=ObjectIdentity
wsLinkStateAlarmNotificationOduDefects=_WsLinkStateAlarmNotificationOduDefects_ObjectIdentity((1,3,6,1,4,1,1271,3,2,12,13))
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduDefects.setStatus(_A)
class _WsLinkStateAlarmNotificationOduOci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduOci_Type.__name__=_D
_WsLinkStateAlarmNotificationOduOci_Object=MibScalar
wsLinkStateAlarmNotificationOduOci=_WsLinkStateAlarmNotificationOduOci_Object((1,3,6,1,4,1,1271,3,2,12,13,1),_WsLinkStateAlarmNotificationOduOci_Type())
wsLinkStateAlarmNotificationOduOci.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduOci.setStatus(_A)
class _WsLinkStateAlarmNotificationOduAis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduAis_Type.__name__=_D
_WsLinkStateAlarmNotificationOduAis_Object=MibScalar
wsLinkStateAlarmNotificationOduAis=_WsLinkStateAlarmNotificationOduAis_Object((1,3,6,1,4,1,1271,3,2,12,13,2),_WsLinkStateAlarmNotificationOduAis_Type())
wsLinkStateAlarmNotificationOduAis.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduAis.setStatus(_A)
class _WsLinkStateAlarmNotificationOduLck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduLck_Type.__name__=_D
_WsLinkStateAlarmNotificationOduLck_Object=MibScalar
wsLinkStateAlarmNotificationOduLck=_WsLinkStateAlarmNotificationOduLck_Object((1,3,6,1,4,1,1271,3,2,12,13,3),_WsLinkStateAlarmNotificationOduLck_Type())
wsLinkStateAlarmNotificationOduLck.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduLck.setStatus(_A)
class _WsLinkStateAlarmNotificationOduSf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduSf_Type.__name__=_D
_WsLinkStateAlarmNotificationOduSf_Object=MibScalar
wsLinkStateAlarmNotificationOduSf=_WsLinkStateAlarmNotificationOduSf_Object((1,3,6,1,4,1,1271,3,2,12,13,4),_WsLinkStateAlarmNotificationOduSf_Type())
wsLinkStateAlarmNotificationOduSf.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduSf.setStatus(_A)
class _WsLinkStateAlarmNotificationOduSd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduSd_Type.__name__=_D
_WsLinkStateAlarmNotificationOduSd_Object=MibScalar
wsLinkStateAlarmNotificationOduSd=_WsLinkStateAlarmNotificationOduSd_Object((1,3,6,1,4,1,1271,3,2,12,13,5),_WsLinkStateAlarmNotificationOduSd_Type())
wsLinkStateAlarmNotificationOduSd.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduSd.setStatus(_A)
class _WsLinkStateAlarmNotificationOduTtiMismatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduTtiMismatch_Type.__name__=_D
_WsLinkStateAlarmNotificationOduTtiMismatch_Object=MibScalar
wsLinkStateAlarmNotificationOduTtiMismatch=_WsLinkStateAlarmNotificationOduTtiMismatch_Object((1,3,6,1,4,1,1271,3,2,12,13,6),_WsLinkStateAlarmNotificationOduTtiMismatch_Type())
wsLinkStateAlarmNotificationOduTtiMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduTtiMismatch.setStatus(_A)
class _WsLinkStateAlarmNotificationOduBdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduBdi_Type.__name__=_D
_WsLinkStateAlarmNotificationOduBdi_Object=MibScalar
wsLinkStateAlarmNotificationOduBdi=_WsLinkStateAlarmNotificationOduBdi_Object((1,3,6,1,4,1,1271,3,2,12,13,7),_WsLinkStateAlarmNotificationOduBdi_Type())
wsLinkStateAlarmNotificationOduBdi.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduBdi.setStatus(_A)
class _WsLinkStateAlarmNotificationOduPtiMismatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduPtiMismatch_Type.__name__=_D
_WsLinkStateAlarmNotificationOduPtiMismatch_Object=MibScalar
wsLinkStateAlarmNotificationOduPtiMismatch=_WsLinkStateAlarmNotificationOduPtiMismatch_Object((1,3,6,1,4,1,1271,3,2,12,13,8),_WsLinkStateAlarmNotificationOduPtiMismatch_Type())
wsLinkStateAlarmNotificationOduPtiMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduPtiMismatch.setStatus(_A)
class _WsLinkStateAlarmNotificationOduFeClientSf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduFeClientSf_Type.__name__=_D
_WsLinkStateAlarmNotificationOduFeClientSf_Object=MibScalar
wsLinkStateAlarmNotificationOduFeClientSf=_WsLinkStateAlarmNotificationOduFeClientSf_Object((1,3,6,1,4,1,1271,3,2,12,13,9),_WsLinkStateAlarmNotificationOduFeClientSf_Type())
wsLinkStateAlarmNotificationOduFeClientSf.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduFeClientSf.setStatus(_A)
class _WsLinkStateAlarmNotificationOduSkewOor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WsLinkStateAlarmNotificationOduSkewOor_Type.__name__=_D
_WsLinkStateAlarmNotificationOduSkewOor_Object=MibScalar
wsLinkStateAlarmNotificationOduSkewOor=_WsLinkStateAlarmNotificationOduSkewOor_Object((1,3,6,1,4,1,1271,3,2,12,13,10),_WsLinkStateAlarmNotificationOduSkewOor_Type())
wsLinkStateAlarmNotificationOduSkewOor.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationOduSkewOor.setStatus(_A)
class _WsLinkStateAlarmNotificationEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('other',1),(_L,2),(_M,3)))
_WsLinkStateAlarmNotificationEntityType_Type.__name__=_D
_WsLinkStateAlarmNotificationEntityType_Object=MibScalar
wsLinkStateAlarmNotificationEntityType=_WsLinkStateAlarmNotificationEntityType_Object((1,3,6,1,4,1,1271,3,2,12,14),_WsLinkStateAlarmNotificationEntityType_Type())
wsLinkStateAlarmNotificationEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:wsLinkStateAlarmNotificationEntityType.setStatus(_A)
wsAlarmNotification=NotificationType((1,3,6,1,4,1,1271,3,2,11))
wsAlarmNotification.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:wsAlarmNotification.setStatus(_A)
wsLinkStateAlarmNotification=NotificationType((1,3,6,1,4,1,1271,3,2,12))
wsLinkStateAlarmNotification.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,'wsLinkStateAlarmNotificationEthEBer'),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,'wsLinkStateAlarmNotificationEthPcsLol'),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:wsLinkStateAlarmNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DisplayString32':DisplayString32,'cienaWsNotificationMIB':cienaWsNotificationMIB,'wsAlarmNotification':wsAlarmNotification,_N:wsAlarmNotificationSiteId,_O:wsAlarmNotificationGroupId,_P:wsAlarmNotificationMemberId,_Q:wsAlarmNotificationInstanceId,_R:wsAlarmNotificationDateAndTime,_S:wsAlarmNotificationTableId,_T:wsAlarmNotificationSeverity,_U:wsAlarmNotificationInstance,_V:wsAlarmNotificationDescription,_W:wsAlarmNotificationActiveStatus,_X:wsAlarmNotificationEntityType,'wsLinkStateAlarmNotification':wsLinkStateAlarmNotification,_Y:wsLinkStateAlarmNotificationSiteId,_Z:wsLinkStateAlarmNotificationGroupId,_a:wsLinkStateAlarmNotificationMemberId,_b:wsLinkStateAlarmNotificationInstanceId,_c:wsLinkStateAlarmNotificationDateAndTime,_d:wsLinkStateAlarmNotificationSeverity,_e:wsLinkStateAlarmNotificationInstance,_f:wsLinkStateAlarmNotificationDescription,'wsLinkStateAlarmNotificationPtpDefects':wsLinkStateAlarmNotificationPtpDefects,_g:wsLinkStateAlarmNotificationPtpRxLos,_h:wsLinkStateAlarmNotificationPtpRxLol,_i:wsLinkStateAlarmNotificationPtpTxLos,_j:wsLinkStateAlarmNotificationPtpTxLol,'wsLinkStateAlarmNotificationEthDefects':wsLinkStateAlarmNotificationEthDefects,'wsLinkStateAlarmNotificationEthPcsHighBer':wsLinkStateAlarmNotificationEthPcsHighBer,_o:wsLinkStateAlarmNotificationEthPcsLoam,_n:wsLinkStateAlarmNotificationEthPcsLobl,_p:wsLinkStateAlarmNotificationEthRsLinkDown,_l:wsLinkStateAlarmNotificationEthRsLf,_m:wsLinkStateAlarmNotificationEthRsRf,_k:wsLinkStateAlarmNotificationEthFecLossSync,'wsLinkStateAlarmNotificationEthPmaSool':wsLinkStateAlarmNotificationEthPmaSool,'wsLinkStateAlarmNotificationOtuDefects':wsLinkStateAlarmNotificationOtuDefects,_q:wsLinkStateAlarmNotificationOtuLoc,_r:wsLinkStateAlarmNotificationOtuFreqOor,_s:wsLinkStateAlarmNotificationOtuLof,_t:wsLinkStateAlarmNotificationOtuPreFecSf,_u:wsLinkStateAlarmNotificationOtuPreFecSd,_v:wsLinkStateAlarmNotificationOtuLom,_w:wsLinkStateAlarmNotificationOtuBdi,_x:wsLinkStateAlarmNotificationOtuTtiMismatch,'wsLinkStateAlarmNotificationOduDefects':wsLinkStateAlarmNotificationOduDefects,_y:wsLinkStateAlarmNotificationOduOci,_z:wsLinkStateAlarmNotificationOduAis,_A0:wsLinkStateAlarmNotificationOduLck,_A1:wsLinkStateAlarmNotificationOduSf,_A2:wsLinkStateAlarmNotificationOduSd,_A3:wsLinkStateAlarmNotificationOduTtiMismatch,_A4:wsLinkStateAlarmNotificationOduBdi,_A5:wsLinkStateAlarmNotificationOduPtiMismatch,_A6:wsLinkStateAlarmNotificationOduFeClientSf,_A7:wsLinkStateAlarmNotificationOduSkewOor,_A8:wsLinkStateAlarmNotificationEntityType})