_J='hpnicfDDosAttackSpeed'
_I='hpnicfDDosAttackThreshold'
_H='hpnicfDDosAttackPolicy'
_G='hpnicfDDosAttackType'
_F='Integer32'
_E='OctetString'
_D='hpnicfDDosAttackTargetIP'
_C='accessible-for-notify'
_B='HPN-ICF-AFC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfAFC=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,85))
if mibBuilder.loadTexts:hpnicfAFC.setRevisions(('2008-07-23 00:00',))
_HpnicfAFCLeaf_ObjectIdentity=ObjectIdentity
hpnicfAFCLeaf=_HpnicfAFCLeaf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,85,1))
_HpnicfDDosAttackTargetIP_Type=IpAddress
_HpnicfDDosAttackTargetIP_Object=MibScalar
hpnicfDDosAttackTargetIP=_HpnicfDDosAttackTargetIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,85,1,1),_HpnicfDDosAttackTargetIP_Type())
hpnicfDDosAttackTargetIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDDosAttackTargetIP.setStatus(_A)
class _HpnicfDDosAttackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15,18,19,20,24,27,29,30,32,33,34,35,36,37,38,39,40,41,42,43,1024)));namedValues=NamedValues(*(('land',1),('smurf',2),('fraggle',3),('winnuke',4),('synflood',5),('icmpflood',6),('udpflood',7),('icmpredirect',8),('icmpunreachable',9),('tracert',11),('tcpflag',12),('pingofdeath',13),('teardrop',14),('ipfragment',15),('largeicmp',18),('sourceroute',19),('routerecord',20),('fragflood',24),('scan',27),('appstreamalarm',29),('sessionstreamalarm',30),('tcpabnormal',32),('ipfragabnormal',33),('tftpabnormal',34),('dnsabnormal',35),('httpabnormal',36),('telnetabnormal',37),('ftpabnormal',38),('smtpabnormal',39),('pop3abnormal',40),('snmpabnormal',41),('ackabnormal',42),('cc',43),('otherabnormal',1024)))
_HpnicfDDosAttackType_Type.__name__=_F
_HpnicfDDosAttackType_Object=MibScalar
hpnicfDDosAttackType=_HpnicfDDosAttackType_Object((1,3,6,1,4,1,11,2,14,11,15,2,85,1,2),_HpnicfDDosAttackType_Type())
hpnicfDDosAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDDosAttackType.setStatus(_A)
class _HpnicfDDosAttackPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnicfDDosAttackPolicy_Type.__name__=_E
_HpnicfDDosAttackPolicy_Object=MibScalar
hpnicfDDosAttackPolicy=_HpnicfDDosAttackPolicy_Object((1,3,6,1,4,1,11,2,14,11,15,2,85,1,3),_HpnicfDDosAttackPolicy_Type())
hpnicfDDosAttackPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDDosAttackPolicy.setStatus(_A)
_HpnicfDDosAttackThreshold_Type=Integer32
_HpnicfDDosAttackThreshold_Object=MibScalar
hpnicfDDosAttackThreshold=_HpnicfDDosAttackThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,85,1,4),_HpnicfDDosAttackThreshold_Type())
hpnicfDDosAttackThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDDosAttackThreshold.setStatus(_A)
_HpnicfDDosAttackSpeed_Type=Integer32
_HpnicfDDosAttackSpeed_Object=MibScalar
hpnicfDDosAttackSpeed=_HpnicfDDosAttackSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,85,1,5),_HpnicfDDosAttackSpeed_Type())
hpnicfDDosAttackSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDDosAttackSpeed.setStatus(_A)
_HpnicfAFCNotify_ObjectIdentity=ObjectIdentity
hpnicfAFCNotify=_HpnicfAFCNotify_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,85,2))
_HpnicfAFCNotifyPrefix_ObjectIdentity=ObjectIdentity
hpnicfAFCNotifyPrefix=_HpnicfAFCNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,85,2,0))
hpnicfDDosAttackStart=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,85,2,0,1))
hpnicfDDosAttackStart.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:hpnicfDDosAttackStart.setStatus(_A)
hpnicfDDosAttackEnd=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,85,2,0,2))
hpnicfDDosAttackEnd.setObjects((_B,_D))
if mibBuilder.loadTexts:hpnicfDDosAttackEnd.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfAFC':hpnicfAFC,'hpnicfAFCLeaf':hpnicfAFCLeaf,_D:hpnicfDDosAttackTargetIP,_G:hpnicfDDosAttackType,_H:hpnicfDDosAttackPolicy,_I:hpnicfDDosAttackThreshold,_J:hpnicfDDosAttackSpeed,'hpnicfAFCNotify':hpnicfAFCNotify,'hpnicfAFCNotifyPrefix':hpnicfAFCNotifyPrefix,'hpnicfDDosAttackStart':hpnicfDDosAttackStart,'hpnicfDDosAttackEnd':hpnicfDDosAttackEnd})