_H='mailalarmCcAddrIdx'
_G='QTECH-GBNPlatformOAMMailalarm-MIB'
_F='disable'
_E='enable'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnPlatformOAM,=mibBuilder.importSymbols('QTECH-GBNPlatformOAM-MIB','gbnPlatformOAM')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnPlatformOAMMailalarm=ModuleIdentity((1,3,6,1,4,1,27514,1,2,1,1,12))
if mibBuilder.loadTexts:gbnPlatformOAMMailalarm.setRevisions(('1905-07-25 00:00',))
class _MailalarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MailalarmState_Type.__name__=_D
_MailalarmState_Object=MibScalar
mailalarmState=_MailalarmState_Object((1,3,6,1,4,1,27514,1,2,1,1,12,1),_MailalarmState_Type())
mailalarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmState.setStatus(_A)
_MailalarmSrvAddr_Type=IpAddress
_MailalarmSrvAddr_Object=MibScalar
mailalarmSrvAddr=_MailalarmSrvAddr_Object((1,3,6,1,4,1,27514,1,2,1,1,12,2),_MailalarmSrvAddr_Type())
mailalarmSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmSrvAddr.setStatus(_A)
class _MailalarmRceiverAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MailalarmRceiverAddr_Type.__name__=_C
_MailalarmRceiverAddr_Object=MibScalar
mailalarmRceiverAddr=_MailalarmRceiverAddr_Object((1,3,6,1,4,1,27514,1,2,1,1,12,3),_MailalarmRceiverAddr_Type())
mailalarmRceiverAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmRceiverAddr.setStatus(_A)
class _MailalarmLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MailalarmLogLevel_Type.__name__=_D
_MailalarmLogLevel_Object=MibScalar
mailalarmLogLevel=_MailalarmLogLevel_Object((1,3,6,1,4,1,27514,1,2,1,1,12,4),_MailalarmLogLevel_Type())
mailalarmLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmLogLevel.setStatus(_A)
class _MailalarmSmtpAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_MailalarmSmtpAuthEnable_Type.__name__=_D
_MailalarmSmtpAuthEnable_Object=MibScalar
mailalarmSmtpAuthEnable=_MailalarmSmtpAuthEnable_Object((1,3,6,1,4,1,27514,1,2,1,1,12,5),_MailalarmSmtpAuthEnable_Type())
mailalarmSmtpAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmSmtpAuthEnable.setStatus(_A)
class _MailalarmSmtpUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MailalarmSmtpUsername_Type.__name__=_C
_MailalarmSmtpUsername_Object=MibScalar
mailalarmSmtpUsername=_MailalarmSmtpUsername_Object((1,3,6,1,4,1,27514,1,2,1,1,12,6),_MailalarmSmtpUsername_Type())
mailalarmSmtpUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmSmtpUsername.setStatus(_A)
class _MailalarmSmtpPasswd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MailalarmSmtpPasswd_Type.__name__=_C
_MailalarmSmtpPasswd_Object=MibScalar
mailalarmSmtpPasswd=_MailalarmSmtpPasswd_Object((1,3,6,1,4,1,27514,1,2,1,1,12,7),_MailalarmSmtpPasswd_Type())
mailalarmSmtpPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmSmtpPasswd.setStatus(_A)
_MailalarmCcAddrTable_Object=MibTable
mailalarmCcAddrTable=_MailalarmCcAddrTable_Object((1,3,6,1,4,1,27514,1,2,1,1,12,8))
if mibBuilder.loadTexts:mailalarmCcAddrTable.setStatus(_A)
_MailalarmCcAddrEntry_Object=MibTableRow
mailalarmCcAddrEntry=_MailalarmCcAddrEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,12,8,1))
mailalarmCcAddrEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:mailalarmCcAddrEntry.setStatus(_A)
class _MailalarmCcAddrIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_MailalarmCcAddrIdx_Type.__name__=_D
_MailalarmCcAddrIdx_Object=MibTableColumn
mailalarmCcAddrIdx=_MailalarmCcAddrIdx_Object((1,3,6,1,4,1,27514,1,2,1,1,12,8,1,1),_MailalarmCcAddrIdx_Type())
mailalarmCcAddrIdx.setMaxAccess('read-only')
if mibBuilder.loadTexts:mailalarmCcAddrIdx.setStatus(_A)
class _MailalarmCcAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_MailalarmCcAddr_Type.__name__=_C
_MailalarmCcAddr_Object=MibTableColumn
mailalarmCcAddr=_MailalarmCcAddr_Object((1,3,6,1,4,1,27514,1,2,1,1,12,8,1,2),_MailalarmCcAddr_Type())
mailalarmCcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mailalarmCcAddr.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'gbnPlatformOAMMailalarm':gbnPlatformOAMMailalarm,'mailalarmState':mailalarmState,'mailalarmSrvAddr':mailalarmSrvAddr,'mailalarmRceiverAddr':mailalarmRceiverAddr,'mailalarmLogLevel':mailalarmLogLevel,'mailalarmSmtpAuthEnable':mailalarmSmtpAuthEnable,'mailalarmSmtpUsername':mailalarmSmtpUsername,'mailalarmSmtpPasswd':mailalarmSmtpPasswd,'mailalarmCcAddrTable':mailalarmCcAddrTable,'mailalarmCcAddrEntry':mailalarmCcAddrEntry,_H:mailalarmCcAddrIdx,'mailalarmCcAddr':mailalarmCcAddr})