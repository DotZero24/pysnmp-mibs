_AM='hpicfNtpConfigGroup'
_AL='hpicfNtpServerNameAssoIsOobm'
_AK='hpicfNtpServerNameAssoBurst'
_AJ='hpicfNtpConfigServerNamePollMaxInterval'
_AI='hpicfNtpConfigServerNamePollMinInterval'
_AH='hpicfNtpInetServerNameAuthKeyId'
_AG='hpicfNtpServerNameResolveStatus'
_AF='hpicfNtpServerNameResolvAddress'
_AE='hpicfNtpServerNameResolvAddType'
_AD='hpicfNtpInetServerNameRowStatus'
_AC='hpicfNtpInetServerName'
_AB='hpicfNtpIpv6MulticastStatus'
_AA='hpicfNtpIpv6Multicast'
_A9='hpicfNtpfiltOffsetSample'
_A8='hpicfNtpfiltDelaySample'
_A7='hpicfNtpAuthenticationKeyRowStatus'
_A6='hpicfNtpAuthenticationKeyTrusted'
_A5='hpicfNtpAuthenticationKeyEncrypted'
_A4='hpicfNtpAuthenticationKeyValue'
_A3='hpicfNtpAuthenticationKeyAuthMode'
_A2='hpicfNtpAssoIsOobm'
_A1='hpicfNtpAssoBurst'
_A0='hpicfNtpAssoPeerDispersion'
_z='hpicfNtpAssoCurrentMode'
_y='hpicfNtpAssoPrecision'
_x='hpicfNtpAssolastPollreq'
_w='hpicfNtpAssoXmtTimeSec'
_v='hpicfNtpAssoXmtTimeFrac'
_u='hpicfNtpAssoRecvTimeSec'
_t='hpicfNtpAssoRecvTimeFrac'
_s='hpicfNtpAssoOriginTimeSec'
_r='hpicfNtpAssoOriginTimeFrac'
_q='hpicfNtpAssoPeerReach'
_p='hpicfNtpAssoRootDispersion'
_o='hpicfNtpAssoRootDelay'
_n='hpicfNtpAssoPeerPollInterval'
_m='hpicfNtpAssoOurPollInterval'
_l='hpicfNtpConfigPollMaxInterval'
_k='hpicfNtpConfigPollMinInterval'
_j='hpicfNtpInetServerAuthKeyId'
_i='hpicfNtpInetServerRowStatus'
_h='hpicfNtpAssoDrift'
_g='hpicfNtpStatusRootDispersion'
_f='hpicfNtpStatusRootDelay'
_e='hpicfNtpStatusClockOffset'
_d='hpicfNtpStatusReferenceTimeSec'
_c='hpicfNtpStatusReferenceTimeFrac'
_b='hpicfNtpAdminStatus'
_a='hpicfNtpMaxAssociation'
_Z='hpicfNtpConfigMode'
_Y='hpicfNtpServerNameIndex'
_X='hpicfNtpAssoSampleId'
_W='hpicfNtpAuthenticationKeyId'
_V='iburst'
_U='noburst'
_T='DisplayString'
_S='ifIndex'
_R='IF-MIB'
_Q='hpicfNtpInetServerNameCfgGroup'
_P='hpicfNtpAssociationSampleGroup'
_O='hpicfNtpAuthenticationKeyIdConfigGroup'
_N='InetAddress'
_M='hpicfNtpInetServerConfigGroup'
_L='hpicfNtpInetServerAddress'
_K='hpicfNtpInetServerAddressType'
_J='not-accessible'
_I='Unsigned32'
_H='TruthValue'
_G='read-write'
_F='Integer32'
_E='OctetString'
_D='read-create'
_C='read-only'
_B='HP-ICF-NTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_R,_S)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','RowStatus','TextualConvention',_H)
hpicfNtpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121))
if mibBuilder.loadTexts:hpicfNtpMIB.setRevisions(('2017-08-22 00:00','2016-02-10 00:00','2015-07-01 00:00'))
_HpicfNtpConfig_ObjectIdentity=ObjectIdentity
hpicfNtpConfig=_HpicfNtpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,1))
_HpicfNtpConfigScalars_ObjectIdentity=ObjectIdentity
hpicfNtpConfigScalars=_HpicfNtpConfigScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1))
class _HpicfNtpConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('unicast',2),('broadcast',3)))
_HpicfNtpConfigMode_Type.__name__=_F
_HpicfNtpConfigMode_Object=MibScalar
hpicfNtpConfigMode=_HpicfNtpConfigMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,1),_HpicfNtpConfigMode_Type())
hpicfNtpConfigMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpConfigMode.setStatus(_A)
class _HpicfNtpMaxAssociation_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpicfNtpMaxAssociation_Type.__name__=_F
_HpicfNtpMaxAssociation_Object=MibScalar
hpicfNtpMaxAssociation=_HpicfNtpMaxAssociation_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,2),_HpicfNtpMaxAssociation_Type())
hpicfNtpMaxAssociation.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpMaxAssociation.setStatus(_A)
_HpicfNtpStatusReferenceTimeFrac_Type=Unsigned32
_HpicfNtpStatusReferenceTimeFrac_Object=MibScalar
hpicfNtpStatusReferenceTimeFrac=_HpicfNtpStatusReferenceTimeFrac_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,3),_HpicfNtpStatusReferenceTimeFrac_Type())
hpicfNtpStatusReferenceTimeFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpStatusReferenceTimeFrac.setStatus(_A)
_HpicfNtpStatusReferenceTimeSec_Type=Unsigned32
_HpicfNtpStatusReferenceTimeSec_Object=MibScalar
hpicfNtpStatusReferenceTimeSec=_HpicfNtpStatusReferenceTimeSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,4),_HpicfNtpStatusReferenceTimeSec_Type())
hpicfNtpStatusReferenceTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpStatusReferenceTimeSec.setStatus(_A)
class _HpicfNtpStatusClockOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpStatusClockOffset_Type.__name__=_E
_HpicfNtpStatusClockOffset_Object=MibScalar
hpicfNtpStatusClockOffset=_HpicfNtpStatusClockOffset_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,5),_HpicfNtpStatusClockOffset_Type())
hpicfNtpStatusClockOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpStatusClockOffset.setStatus(_A)
class _HpicfNtpStatusRootDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpStatusRootDelay_Type.__name__=_E
_HpicfNtpStatusRootDelay_Object=MibScalar
hpicfNtpStatusRootDelay=_HpicfNtpStatusRootDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,6),_HpicfNtpStatusRootDelay_Type())
hpicfNtpStatusRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpStatusRootDelay.setStatus(_A)
class _HpicfNtpStatusRootDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpStatusRootDispersion_Type.__name__=_E
_HpicfNtpStatusRootDispersion_Object=MibScalar
hpicfNtpStatusRootDispersion=_HpicfNtpStatusRootDispersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,7),_HpicfNtpStatusRootDispersion_Type())
hpicfNtpStatusRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpStatusRootDispersion.setStatus(_A)
class _HpicfNtpAssoDrift_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpAssoDrift_Type.__name__=_E
_HpicfNtpAssoDrift_Object=MibScalar
hpicfNtpAssoDrift=_HpicfNtpAssoDrift_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,1,8),_HpicfNtpAssoDrift_Type())
hpicfNtpAssoDrift.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoDrift.setStatus(_A)
_HpicfNtpInetConfigServerTable_Object=MibTable
hpicfNtpInetConfigServerTable=_HpicfNtpInetConfigServerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2))
if mibBuilder.loadTexts:hpicfNtpInetConfigServerTable.setStatus(_A)
_HpicfNtpInetConfigServerEntry_Object=MibTableRow
hpicfNtpInetConfigServerEntry=_HpicfNtpInetConfigServerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1))
hpicfNtpInetConfigServerEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpicfNtpInetConfigServerEntry.setStatus(_A)
_HpicfNtpInetServerAddressType_Type=InetAddressType
_HpicfNtpInetServerAddressType_Object=MibTableColumn
hpicfNtpInetServerAddressType=_HpicfNtpInetServerAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,1),_HpicfNtpInetServerAddressType_Type())
hpicfNtpInetServerAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfNtpInetServerAddressType.setStatus(_A)
class _HpicfNtpInetServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_HpicfNtpInetServerAddress_Type.__name__=_N
_HpicfNtpInetServerAddress_Object=MibTableColumn
hpicfNtpInetServerAddress=_HpicfNtpInetServerAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,2),_HpicfNtpInetServerAddress_Type())
hpicfNtpInetServerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfNtpInetServerAddress.setStatus(_A)
_HpicfNtpInetServerRowStatus_Type=RowStatus
_HpicfNtpInetServerRowStatus_Object=MibTableColumn
hpicfNtpInetServerRowStatus=_HpicfNtpInetServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,4),_HpicfNtpInetServerRowStatus_Type())
hpicfNtpInetServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpInetServerRowStatus.setStatus(_A)
class _HpicfNtpInetServerAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfNtpInetServerAuthKeyId_Type.__name__=_I
_HpicfNtpInetServerAuthKeyId_Object=MibTableColumn
hpicfNtpInetServerAuthKeyId=_HpicfNtpInetServerAuthKeyId_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,5),_HpicfNtpInetServerAuthKeyId_Type())
hpicfNtpInetServerAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpInetServerAuthKeyId.setStatus(_A)
class _HpicfNtpConfigPollMinInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,17))
_HpicfNtpConfigPollMinInterval_Type.__name__=_F
_HpicfNtpConfigPollMinInterval_Object=MibTableColumn
hpicfNtpConfigPollMinInterval=_HpicfNtpConfigPollMinInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,6),_HpicfNtpConfigPollMinInterval_Type())
hpicfNtpConfigPollMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpConfigPollMinInterval.setStatus(_A)
class _HpicfNtpConfigPollMaxInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,17))
_HpicfNtpConfigPollMaxInterval_Type.__name__=_F
_HpicfNtpConfigPollMaxInterval_Object=MibTableColumn
hpicfNtpConfigPollMaxInterval=_HpicfNtpConfigPollMaxInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,7),_HpicfNtpConfigPollMaxInterval_Type())
hpicfNtpConfigPollMaxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpConfigPollMaxInterval.setStatus(_A)
class _HpicfNtpAssoBurst_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('burst',2),(_V,3)))
_HpicfNtpAssoBurst_Type.__name__=_F
_HpicfNtpAssoBurst_Object=MibTableColumn
hpicfNtpAssoBurst=_HpicfNtpAssoBurst_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,8),_HpicfNtpAssoBurst_Type())
hpicfNtpAssoBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAssoBurst.setStatus(_A)
class _HpicfNtpAssoIsOobm_Type(TruthValue):defaultValue=2
_HpicfNtpAssoIsOobm_Type.__name__=_H
_HpicfNtpAssoIsOobm_Object=MibTableColumn
hpicfNtpAssoIsOobm=_HpicfNtpAssoIsOobm_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,2,1,9),_HpicfNtpAssoIsOobm_Type())
hpicfNtpAssoIsOobm.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAssoIsOobm.setStatus(_A)
_HpicfNtpInetServerInfoTable_Object=MibTable
hpicfNtpInetServerInfoTable=_HpicfNtpInetServerInfoTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3))
if mibBuilder.loadTexts:hpicfNtpInetServerInfoTable.setStatus(_A)
_HpicfNtpInetServerInfoEntry_Object=MibTableRow
hpicfNtpInetServerInfoEntry=_HpicfNtpInetServerInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1))
hpicfNtpInetServerInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpicfNtpInetServerInfoEntry.setStatus(_A)
_HpicfNtpAssoOurPollInterval_Type=Integer32
_HpicfNtpAssoOurPollInterval_Object=MibTableColumn
hpicfNtpAssoOurPollInterval=_HpicfNtpAssoOurPollInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,1),_HpicfNtpAssoOurPollInterval_Type())
hpicfNtpAssoOurPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoOurPollInterval.setStatus(_A)
_HpicfNtpAssoPeerPollInterval_Type=Integer32
_HpicfNtpAssoPeerPollInterval_Object=MibTableColumn
hpicfNtpAssoPeerPollInterval=_HpicfNtpAssoPeerPollInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,2),_HpicfNtpAssoPeerPollInterval_Type())
hpicfNtpAssoPeerPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoPeerPollInterval.setStatus(_A)
class _HpicfNtpAssoRootDelay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpAssoRootDelay_Type.__name__=_E
_HpicfNtpAssoRootDelay_Object=MibTableColumn
hpicfNtpAssoRootDelay=_HpicfNtpAssoRootDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,3),_HpicfNtpAssoRootDelay_Type())
hpicfNtpAssoRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoRootDelay.setStatus(_A)
class _HpicfNtpAssoRootDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpAssoRootDispersion_Type.__name__=_E
_HpicfNtpAssoRootDispersion_Object=MibTableColumn
hpicfNtpAssoRootDispersion=_HpicfNtpAssoRootDispersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,4),_HpicfNtpAssoRootDispersion_Type())
hpicfNtpAssoRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoRootDispersion.setStatus(_A)
class _HpicfNtpAssoPeerReach_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpAssoPeerReach_Type.__name__=_E
_HpicfNtpAssoPeerReach_Object=MibTableColumn
hpicfNtpAssoPeerReach=_HpicfNtpAssoPeerReach_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,6),_HpicfNtpAssoPeerReach_Type())
hpicfNtpAssoPeerReach.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoPeerReach.setStatus(_A)
_HpicfNtpAssoOriginTimeFrac_Type=Unsigned32
_HpicfNtpAssoOriginTimeFrac_Object=MibTableColumn
hpicfNtpAssoOriginTimeFrac=_HpicfNtpAssoOriginTimeFrac_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,7),_HpicfNtpAssoOriginTimeFrac_Type())
hpicfNtpAssoOriginTimeFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoOriginTimeFrac.setStatus(_A)
_HpicfNtpAssoOriginTimeSec_Type=Unsigned32
_HpicfNtpAssoOriginTimeSec_Object=MibTableColumn
hpicfNtpAssoOriginTimeSec=_HpicfNtpAssoOriginTimeSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,8),_HpicfNtpAssoOriginTimeSec_Type())
hpicfNtpAssoOriginTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoOriginTimeSec.setStatus(_A)
_HpicfNtpAssoRecvTimeFrac_Type=Unsigned32
_HpicfNtpAssoRecvTimeFrac_Object=MibTableColumn
hpicfNtpAssoRecvTimeFrac=_HpicfNtpAssoRecvTimeFrac_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,9),_HpicfNtpAssoRecvTimeFrac_Type())
hpicfNtpAssoRecvTimeFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoRecvTimeFrac.setStatus(_A)
_HpicfNtpAssoRecvTimeSec_Type=Unsigned32
_HpicfNtpAssoRecvTimeSec_Object=MibTableColumn
hpicfNtpAssoRecvTimeSec=_HpicfNtpAssoRecvTimeSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,10),_HpicfNtpAssoRecvTimeSec_Type())
hpicfNtpAssoRecvTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoRecvTimeSec.setStatus(_A)
_HpicfNtpAssoXmtTimeFrac_Type=Unsigned32
_HpicfNtpAssoXmtTimeFrac_Object=MibTableColumn
hpicfNtpAssoXmtTimeFrac=_HpicfNtpAssoXmtTimeFrac_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,11),_HpicfNtpAssoXmtTimeFrac_Type())
hpicfNtpAssoXmtTimeFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoXmtTimeFrac.setStatus(_A)
_HpicfNtpAssoXmtTimeSec_Type=Unsigned32
_HpicfNtpAssoXmtTimeSec_Object=MibTableColumn
hpicfNtpAssoXmtTimeSec=_HpicfNtpAssoXmtTimeSec_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,12),_HpicfNtpAssoXmtTimeSec_Type())
hpicfNtpAssoXmtTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoXmtTimeSec.setStatus(_A)
_HpicfNtpAssolastPollreq_Type=Integer32
_HpicfNtpAssolastPollreq_Object=MibTableColumn
hpicfNtpAssolastPollreq=_HpicfNtpAssolastPollreq_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,13),_HpicfNtpAssolastPollreq_Type())
hpicfNtpAssolastPollreq.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssolastPollreq.setStatus(_A)
_HpicfNtpAssoPrecision_Type=Integer32
_HpicfNtpAssoPrecision_Object=MibTableColumn
hpicfNtpAssoPrecision=_HpicfNtpAssoPrecision_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,14),_HpicfNtpAssoPrecision_Type())
hpicfNtpAssoPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoPrecision.setStatus(_A)
class _HpicfNtpAssoCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('synchronized',1),('notsynchronized',2),('unknown',99)))
_HpicfNtpAssoCurrentMode_Type.__name__=_F
_HpicfNtpAssoCurrentMode_Object=MibTableColumn
hpicfNtpAssoCurrentMode=_HpicfNtpAssoCurrentMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,15),_HpicfNtpAssoCurrentMode_Type())
hpicfNtpAssoCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoCurrentMode.setStatus(_A)
class _HpicfNtpAssoPeerDispersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpAssoPeerDispersion_Type.__name__=_E
_HpicfNtpAssoPeerDispersion_Object=MibTableColumn
hpicfNtpAssoPeerDispersion=_HpicfNtpAssoPeerDispersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,3,1,16),_HpicfNtpAssoPeerDispersion_Type())
hpicfNtpAssoPeerDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpAssoPeerDispersion.setStatus(_A)
_HpicfNtpAuthenticationKeyTable_Object=MibTable
hpicfNtpAuthenticationKeyTable=_HpicfNtpAuthenticationKeyTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4))
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyTable.setStatus(_A)
_HpicfNtpAuthenticationKeyEntry_Object=MibTableRow
hpicfNtpAuthenticationKeyEntry=_HpicfNtpAuthenticationKeyEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1))
hpicfNtpAuthenticationKeyEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyEntry.setStatus(_A)
class _HpicfNtpAuthenticationKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpicfNtpAuthenticationKeyId_Type.__name__=_I
_HpicfNtpAuthenticationKeyId_Object=MibTableColumn
hpicfNtpAuthenticationKeyId=_HpicfNtpAuthenticationKeyId_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,1),_HpicfNtpAuthenticationKeyId_Type())
hpicfNtpAuthenticationKeyId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyId.setStatus(_A)
class _HpicfNtpAuthenticationKeyAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('md5',2),('sha1',3)))
_HpicfNtpAuthenticationKeyAuthMode_Type.__name__=_F
_HpicfNtpAuthenticationKeyAuthMode_Object=MibTableColumn
hpicfNtpAuthenticationKeyAuthMode=_HpicfNtpAuthenticationKeyAuthMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,2),_HpicfNtpAuthenticationKeyAuthMode_Type())
hpicfNtpAuthenticationKeyAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyAuthMode.setStatus(_A)
class _HpicfNtpAuthenticationKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfNtpAuthenticationKeyValue_Type.__name__=_E
_HpicfNtpAuthenticationKeyValue_Object=MibTableColumn
hpicfNtpAuthenticationKeyValue=_HpicfNtpAuthenticationKeyValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,3),_HpicfNtpAuthenticationKeyValue_Type())
hpicfNtpAuthenticationKeyValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyValue.setStatus(_A)
class _HpicfNtpAuthenticationKeyTrusted_Type(TruthValue):defaultValue=2
_HpicfNtpAuthenticationKeyTrusted_Type.__name__=_H
_HpicfNtpAuthenticationKeyTrusted_Object=MibTableColumn
hpicfNtpAuthenticationKeyTrusted=_HpicfNtpAuthenticationKeyTrusted_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,4),_HpicfNtpAuthenticationKeyTrusted_Type())
hpicfNtpAuthenticationKeyTrusted.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyTrusted.setStatus(_A)
_HpicfNtpAuthenticationKeyRowStatus_Type=RowStatus
_HpicfNtpAuthenticationKeyRowStatus_Object=MibTableColumn
hpicfNtpAuthenticationKeyRowStatus=_HpicfNtpAuthenticationKeyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,5),_HpicfNtpAuthenticationKeyRowStatus_Type())
hpicfNtpAuthenticationKeyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyRowStatus.setStatus(_A)
class _HpicfNtpAuthenticationKeyEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfNtpAuthenticationKeyEncrypted_Type.__name__=_E
_HpicfNtpAuthenticationKeyEncrypted_Object=MibTableColumn
hpicfNtpAuthenticationKeyEncrypted=_HpicfNtpAuthenticationKeyEncrypted_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,4,1,6),_HpicfNtpAuthenticationKeyEncrypted_Type())
hpicfNtpAuthenticationKeyEncrypted.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyEncrypted.setStatus(_A)
_HpicfNtpIpv6MulticastTable_Object=MibTable
hpicfNtpIpv6MulticastTable=_HpicfNtpIpv6MulticastTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,5))
if mibBuilder.loadTexts:hpicfNtpIpv6MulticastTable.setStatus(_A)
_HpicfNtpIpv6MulticastEntry_Object=MibTableRow
hpicfNtpIpv6MulticastEntry=_HpicfNtpIpv6MulticastEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,5,1))
hpicfNtpIpv6MulticastEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:hpicfNtpIpv6MulticastEntry.setStatus(_A)
class _HpicfNtpIpv6Multicast_Type(TruthValue):defaultValue=2
_HpicfNtpIpv6Multicast_Type.__name__=_H
_HpicfNtpIpv6Multicast_Object=MibTableColumn
hpicfNtpIpv6Multicast=_HpicfNtpIpv6Multicast_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,5,1,1),_HpicfNtpIpv6Multicast_Type())
hpicfNtpIpv6Multicast.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpIpv6Multicast.setStatus(_A)
_HpicfNtpIpv6MulticastStatus_Type=RowStatus
_HpicfNtpIpv6MulticastStatus_Object=MibTableColumn
hpicfNtpIpv6MulticastStatus=_HpicfNtpIpv6MulticastStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,5,1,2),_HpicfNtpIpv6MulticastStatus_Type())
hpicfNtpIpv6MulticastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpIpv6MulticastStatus.setStatus(_A)
_HpicfNtpAssoSampleTable_Object=MibTable
hpicfNtpAssoSampleTable=_HpicfNtpAssoSampleTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,7))
if mibBuilder.loadTexts:hpicfNtpAssoSampleTable.setStatus(_A)
_HpicfNtpAssoSampleEntry_Object=MibTableRow
hpicfNtpAssoSampleEntry=_HpicfNtpAssoSampleEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,7,1))
hpicfNtpAssoSampleEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_X))
if mibBuilder.loadTexts:hpicfNtpAssoSampleEntry.setStatus(_A)
_HpicfNtpAssoSampleId_Type=Unsigned32
_HpicfNtpAssoSampleId_Object=MibTableColumn
hpicfNtpAssoSampleId=_HpicfNtpAssoSampleId_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,7,1,1),_HpicfNtpAssoSampleId_Type())
hpicfNtpAssoSampleId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfNtpAssoSampleId.setStatus(_A)
class _HpicfNtpfiltDelaySample_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpfiltDelaySample_Type.__name__=_E
_HpicfNtpfiltDelaySample_Object=MibTableColumn
hpicfNtpfiltDelaySample=_HpicfNtpfiltDelaySample_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,7,1,2),_HpicfNtpfiltDelaySample_Type())
hpicfNtpfiltDelaySample.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpfiltDelaySample.setStatus(_A)
class _HpicfNtpfiltOffsetSample_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_HpicfNtpfiltOffsetSample_Type.__name__=_E
_HpicfNtpfiltOffsetSample_Object=MibTableColumn
hpicfNtpfiltOffsetSample=_HpicfNtpfiltOffsetSample_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,7,1,3),_HpicfNtpfiltOffsetSample_Type())
hpicfNtpfiltOffsetSample.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpfiltOffsetSample.setStatus(_A)
_HpicfNtpInetServerNameTable_Object=MibTable
hpicfNtpInetServerNameTable=_HpicfNtpInetServerNameTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8))
if mibBuilder.loadTexts:hpicfNtpInetServerNameTable.setStatus(_A)
_HpicfNtpInetServerNameEntry_Object=MibTableRow
hpicfNtpInetServerNameEntry=_HpicfNtpInetServerNameEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1))
hpicfNtpInetServerNameEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:hpicfNtpInetServerNameEntry.setStatus(_A)
class _HpicfNtpServerNameIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpicfNtpServerNameIndex_Type.__name__=_I
_HpicfNtpServerNameIndex_Object=MibTableColumn
hpicfNtpServerNameIndex=_HpicfNtpServerNameIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,1),_HpicfNtpServerNameIndex_Type())
hpicfNtpServerNameIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpicfNtpServerNameIndex.setStatus(_A)
class _HpicfNtpInetServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpicfNtpInetServerName_Type.__name__=_T
_HpicfNtpInetServerName_Object=MibTableColumn
hpicfNtpInetServerName=_HpicfNtpInetServerName_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,2),_HpicfNtpInetServerName_Type())
hpicfNtpInetServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpInetServerName.setStatus(_A)
_HpicfNtpInetServerNameRowStatus_Type=RowStatus
_HpicfNtpInetServerNameRowStatus_Object=MibTableColumn
hpicfNtpInetServerNameRowStatus=_HpicfNtpInetServerNameRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,3),_HpicfNtpInetServerNameRowStatus_Type())
hpicfNtpInetServerNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfNtpInetServerNameRowStatus.setStatus(_A)
_HpicfNtpServerNameResolvAddType_Type=InetAddressType
_HpicfNtpServerNameResolvAddType_Object=MibTableColumn
hpicfNtpServerNameResolvAddType=_HpicfNtpServerNameResolvAddType_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,4),_HpicfNtpServerNameResolvAddType_Type())
hpicfNtpServerNameResolvAddType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpServerNameResolvAddType.setStatus(_A)
class _HpicfNtpServerNameResolvAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_HpicfNtpServerNameResolvAddress_Type.__name__=_N
_HpicfNtpServerNameResolvAddress_Object=MibTableColumn
hpicfNtpServerNameResolvAddress=_HpicfNtpServerNameResolvAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,5),_HpicfNtpServerNameResolvAddress_Type())
hpicfNtpServerNameResolvAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpServerNameResolvAddress.setStatus(_A)
class _HpicfNtpServerNameResolveStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notattempted',0),('active',1),('dnsunknownhost',2),('dnsnotresponding',3),('dnsfailed',4),('notactive',5)))
_HpicfNtpServerNameResolveStatus_Type.__name__=_F
_HpicfNtpServerNameResolveStatus_Object=MibTableColumn
hpicfNtpServerNameResolveStatus=_HpicfNtpServerNameResolveStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,6),_HpicfNtpServerNameResolveStatus_Type())
hpicfNtpServerNameResolveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfNtpServerNameResolveStatus.setStatus(_A)
class _HpicfNtpInetServerNameAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfNtpInetServerNameAuthKeyId_Type.__name__=_I
_HpicfNtpInetServerNameAuthKeyId_Object=MibTableColumn
hpicfNtpInetServerNameAuthKeyId=_HpicfNtpInetServerNameAuthKeyId_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,7),_HpicfNtpInetServerNameAuthKeyId_Type())
hpicfNtpInetServerNameAuthKeyId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpInetServerNameAuthKeyId.setStatus(_A)
class _HpicfNtpConfigServerNamePollMinInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,17))
_HpicfNtpConfigServerNamePollMinInterval_Type.__name__=_F
_HpicfNtpConfigServerNamePollMinInterval_Object=MibTableColumn
hpicfNtpConfigServerNamePollMinInterval=_HpicfNtpConfigServerNamePollMinInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,8),_HpicfNtpConfigServerNamePollMinInterval_Type())
hpicfNtpConfigServerNamePollMinInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpConfigServerNamePollMinInterval.setStatus(_A)
class _HpicfNtpConfigServerNamePollMaxInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,17))
_HpicfNtpConfigServerNamePollMaxInterval_Type.__name__=_F
_HpicfNtpConfigServerNamePollMaxInterval_Object=MibTableColumn
hpicfNtpConfigServerNamePollMaxInterval=_HpicfNtpConfigServerNamePollMaxInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,9),_HpicfNtpConfigServerNamePollMaxInterval_Type())
hpicfNtpConfigServerNamePollMaxInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpConfigServerNamePollMaxInterval.setStatus(_A)
class _HpicfNtpServerNameAssoBurst_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('burst',2),(_V,3)))
_HpicfNtpServerNameAssoBurst_Type.__name__=_F
_HpicfNtpServerNameAssoBurst_Object=MibTableColumn
hpicfNtpServerNameAssoBurst=_HpicfNtpServerNameAssoBurst_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,10),_HpicfNtpServerNameAssoBurst_Type())
hpicfNtpServerNameAssoBurst.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpServerNameAssoBurst.setStatus(_A)
class _HpicfNtpServerNameAssoIsOobm_Type(TruthValue):defaultValue=2
_HpicfNtpServerNameAssoIsOobm_Type.__name__=_H
_HpicfNtpServerNameAssoIsOobm_Object=MibTableColumn
hpicfNtpServerNameAssoIsOobm=_HpicfNtpServerNameAssoIsOobm_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,1,8,1,11),_HpicfNtpServerNameAssoIsOobm_Type())
hpicfNtpServerNameAssoIsOobm.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpServerNameAssoIsOobm.setStatus(_A)
_HpicfNtpGlobal_ObjectIdentity=ObjectIdentity
hpicfNtpGlobal=_HpicfNtpGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,2))
class _HpicfNtpAdminStatus_Type(TruthValue):defaultValue=2
_HpicfNtpAdminStatus_Type.__name__=_H
_HpicfNtpAdminStatus_Object=MibScalar
hpicfNtpAdminStatus=_HpicfNtpAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,121,2,1),_HpicfNtpAdminStatus_Type())
hpicfNtpAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfNtpAdminStatus.setStatus(_A)
_HpicfNtpConfigConformance_ObjectIdentity=ObjectIdentity
hpicfNtpConfigConformance=_HpicfNtpConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,3))
_HpicfNtpConfigCompliances_ObjectIdentity=ObjectIdentity
hpicfNtpConfigCompliances=_HpicfNtpConfigCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1))
_HpicfNtpConfigGroups_ObjectIdentity=ObjectIdentity
hpicfNtpConfigGroups=_HpicfNtpConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2))
hpicfNtpConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2,1))
hpicfNtpConfigGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:hpicfNtpConfigGroup.setStatus(_A)
hpicfNtpInetServerConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2,2))
hpicfNtpInetServerConfigGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:hpicfNtpInetServerConfigGroup.setStatus(_A)
hpicfNtpAuthenticationKeyIdConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2,3))
hpicfNtpAuthenticationKeyIdConfigGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:hpicfNtpAuthenticationKeyIdConfigGroup.setStatus(_A)
hpicfNtpAssociationSampleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2,4))
hpicfNtpAssociationSampleGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:hpicfNtpAssociationSampleGroup.setStatus(_A)
hpicfNtpInetServerNameCfgGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,121,3,2,5))
hpicfNtpInetServerNameCfgGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:hpicfNtpInetServerNameCfgGroup.setStatus(_A)
hpicfNtpInetConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1,1))
hpicfNtpInetConfigCompliance.setObjects(*((_B,_AM),(_B,_M)))
if mibBuilder.loadTexts:hpicfNtpInetConfigCompliance.setStatus(_A)
hpicfNtpAuthenticationConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1,2))
hpicfNtpAuthenticationConfigCompliance.setObjects(*((_B,_O),(_B,_O)))
if mibBuilder.loadTexts:hpicfNtpAuthenticationConfigCompliance.setStatus(_A)
hpicfNtpServerConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1,3))
hpicfNtpServerConfigCompliance.setObjects(*((_B,_M),(_B,_M)))
if mibBuilder.loadTexts:hpicfNtpServerConfigCompliance.setStatus(_A)
hpicfNtpAssoSampleCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1,4))
hpicfNtpAssoSampleCompliance.setObjects(*((_B,_P),(_B,_P)))
if mibBuilder.loadTexts:hpicfNtpAssoSampleCompliance.setStatus(_A)
hpicfNtpServerNameCfgCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,121,3,1,5))
hpicfNtpServerNameCfgCompliance.setObjects(*((_B,_Q),(_B,_Q)))
if mibBuilder.loadTexts:hpicfNtpServerNameCfgCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfNtpMIB':hpicfNtpMIB,'hpicfNtpConfig':hpicfNtpConfig,'hpicfNtpConfigScalars':hpicfNtpConfigScalars,_Z:hpicfNtpConfigMode,_a:hpicfNtpMaxAssociation,_c:hpicfNtpStatusReferenceTimeFrac,_d:hpicfNtpStatusReferenceTimeSec,_e:hpicfNtpStatusClockOffset,_f:hpicfNtpStatusRootDelay,_g:hpicfNtpStatusRootDispersion,_h:hpicfNtpAssoDrift,'hpicfNtpInetConfigServerTable':hpicfNtpInetConfigServerTable,'hpicfNtpInetConfigServerEntry':hpicfNtpInetConfigServerEntry,_K:hpicfNtpInetServerAddressType,_L:hpicfNtpInetServerAddress,_i:hpicfNtpInetServerRowStatus,_j:hpicfNtpInetServerAuthKeyId,_k:hpicfNtpConfigPollMinInterval,_l:hpicfNtpConfigPollMaxInterval,_A1:hpicfNtpAssoBurst,_A2:hpicfNtpAssoIsOobm,'hpicfNtpInetServerInfoTable':hpicfNtpInetServerInfoTable,'hpicfNtpInetServerInfoEntry':hpicfNtpInetServerInfoEntry,_m:hpicfNtpAssoOurPollInterval,_n:hpicfNtpAssoPeerPollInterval,_o:hpicfNtpAssoRootDelay,_p:hpicfNtpAssoRootDispersion,_q:hpicfNtpAssoPeerReach,_r:hpicfNtpAssoOriginTimeFrac,_s:hpicfNtpAssoOriginTimeSec,_t:hpicfNtpAssoRecvTimeFrac,_u:hpicfNtpAssoRecvTimeSec,_v:hpicfNtpAssoXmtTimeFrac,_w:hpicfNtpAssoXmtTimeSec,_x:hpicfNtpAssolastPollreq,_y:hpicfNtpAssoPrecision,_z:hpicfNtpAssoCurrentMode,_A0:hpicfNtpAssoPeerDispersion,'hpicfNtpAuthenticationKeyTable':hpicfNtpAuthenticationKeyTable,'hpicfNtpAuthenticationKeyEntry':hpicfNtpAuthenticationKeyEntry,_W:hpicfNtpAuthenticationKeyId,_A3:hpicfNtpAuthenticationKeyAuthMode,_A4:hpicfNtpAuthenticationKeyValue,_A6:hpicfNtpAuthenticationKeyTrusted,_A7:hpicfNtpAuthenticationKeyRowStatus,_A5:hpicfNtpAuthenticationKeyEncrypted,'hpicfNtpIpv6MulticastTable':hpicfNtpIpv6MulticastTable,'hpicfNtpIpv6MulticastEntry':hpicfNtpIpv6MulticastEntry,_AA:hpicfNtpIpv6Multicast,_AB:hpicfNtpIpv6MulticastStatus,'hpicfNtpAssoSampleTable':hpicfNtpAssoSampleTable,'hpicfNtpAssoSampleEntry':hpicfNtpAssoSampleEntry,_X:hpicfNtpAssoSampleId,_A8:hpicfNtpfiltDelaySample,_A9:hpicfNtpfiltOffsetSample,'hpicfNtpInetServerNameTable':hpicfNtpInetServerNameTable,'hpicfNtpInetServerNameEntry':hpicfNtpInetServerNameEntry,_Y:hpicfNtpServerNameIndex,_AC:hpicfNtpInetServerName,_AD:hpicfNtpInetServerNameRowStatus,_AE:hpicfNtpServerNameResolvAddType,_AF:hpicfNtpServerNameResolvAddress,_AG:hpicfNtpServerNameResolveStatus,_AH:hpicfNtpInetServerNameAuthKeyId,_AI:hpicfNtpConfigServerNamePollMinInterval,_AJ:hpicfNtpConfigServerNamePollMaxInterval,_AK:hpicfNtpServerNameAssoBurst,_AL:hpicfNtpServerNameAssoIsOobm,'hpicfNtpGlobal':hpicfNtpGlobal,_b:hpicfNtpAdminStatus,'hpicfNtpConfigConformance':hpicfNtpConfigConformance,'hpicfNtpConfigCompliances':hpicfNtpConfigCompliances,'hpicfNtpInetConfigCompliance':hpicfNtpInetConfigCompliance,'hpicfNtpAuthenticationConfigCompliance':hpicfNtpAuthenticationConfigCompliance,'hpicfNtpServerConfigCompliance':hpicfNtpServerConfigCompliance,'hpicfNtpAssoSampleCompliance':hpicfNtpAssoSampleCompliance,'hpicfNtpServerNameCfgCompliance':hpicfNtpServerNameCfgCompliance,'hpicfNtpConfigGroups':hpicfNtpConfigGroups,_AM:hpicfNtpConfigGroup,_M:hpicfNtpInetServerConfigGroup,_O:hpicfNtpAuthenticationKeyIdConfigGroup,_P:hpicfNtpAssociationSampleGroup,_Q:hpicfNtpInetServerNameCfgGroup})