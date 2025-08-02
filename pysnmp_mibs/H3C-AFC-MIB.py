_J='h3cDDosAttackSpeed'
_I='h3cDDosAttackThreshold'
_H='h3cDDosAttackPolicy'
_G='h3cDDosAttackType'
_F='Integer32'
_E='OctetString'
_D='h3cDDosAttackTargetIP'
_C='accessible-for-notify'
_B='H3C-AFC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cAFC=ModuleIdentity((1,3,6,1,4,1,2011,10,2,85))
if mibBuilder.loadTexts:h3cAFC.setRevisions(('2008-07-23 00:00',))
_H3cAFCLeaf_ObjectIdentity=ObjectIdentity
h3cAFCLeaf=_H3cAFCLeaf_ObjectIdentity((1,3,6,1,4,1,2011,10,2,85,1))
_H3cDDosAttackTargetIP_Type=IpAddress
_H3cDDosAttackTargetIP_Object=MibScalar
h3cDDosAttackTargetIP=_H3cDDosAttackTargetIP_Object((1,3,6,1,4,1,2011,10,2,85,1,1),_H3cDDosAttackTargetIP_Type())
h3cDDosAttackTargetIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDDosAttackTargetIP.setStatus(_A)
class _H3cDDosAttackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15,18,19,20,24,27,29,30,32,33,34,35,36,37,38,39,40,41,42,43,1024)));namedValues=NamedValues(*(('land',1),('smurf',2),('fraggle',3),('winnuke',4),('synflood',5),('icmpflood',6),('udpflood',7),('icmpredirect',8),('icmpunreachable',9),('tracert',11),('tcpflag',12),('pingofdeath',13),('teardrop',14),('ipfragment',15),('largeicmp',18),('sourceroute',19),('routerecord',20),('fragflood',24),('scan',27),('appstreamalarm',29),('sessionstreamalarm',30),('tcpabnormal',32),('ipfragabnormal',33),('tftpabnormal',34),('dnsabnormal',35),('httpabnormal',36),('telnetabnormal',37),('ftpabnormal',38),('smtpabnormal',39),('pop3abnormal',40),('snmpabnormal',41),('ackabnormal',42),('cc',43),('otherabnormal',1024)))
_H3cDDosAttackType_Type.__name__=_F
_H3cDDosAttackType_Object=MibScalar
h3cDDosAttackType=_H3cDDosAttackType_Object((1,3,6,1,4,1,2011,10,2,85,1,2),_H3cDDosAttackType_Type())
h3cDDosAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDDosAttackType.setStatus(_A)
class _H3cDDosAttackPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_H3cDDosAttackPolicy_Type.__name__=_E
_H3cDDosAttackPolicy_Object=MibScalar
h3cDDosAttackPolicy=_H3cDDosAttackPolicy_Object((1,3,6,1,4,1,2011,10,2,85,1,3),_H3cDDosAttackPolicy_Type())
h3cDDosAttackPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDDosAttackPolicy.setStatus(_A)
_H3cDDosAttackThreshold_Type=Integer32
_H3cDDosAttackThreshold_Object=MibScalar
h3cDDosAttackThreshold=_H3cDDosAttackThreshold_Object((1,3,6,1,4,1,2011,10,2,85,1,4),_H3cDDosAttackThreshold_Type())
h3cDDosAttackThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDDosAttackThreshold.setStatus(_A)
_H3cDDosAttackSpeed_Type=Integer32
_H3cDDosAttackSpeed_Object=MibScalar
h3cDDosAttackSpeed=_H3cDDosAttackSpeed_Object((1,3,6,1,4,1,2011,10,2,85,1,5),_H3cDDosAttackSpeed_Type())
h3cDDosAttackSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDDosAttackSpeed.setStatus(_A)
_H3cAFCNotify_ObjectIdentity=ObjectIdentity
h3cAFCNotify=_H3cAFCNotify_ObjectIdentity((1,3,6,1,4,1,2011,10,2,85,2))
_H3cAFCNotifyPrefix_ObjectIdentity=ObjectIdentity
h3cAFCNotifyPrefix=_H3cAFCNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,85,2,0))
h3cDDosAttackStart=NotificationType((1,3,6,1,4,1,2011,10,2,85,2,0,1))
h3cDDosAttackStart.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:h3cDDosAttackStart.setStatus(_A)
h3cDDosAttackEnd=NotificationType((1,3,6,1,4,1,2011,10,2,85,2,0,2))
h3cDDosAttackEnd.setObjects((_B,_D))
if mibBuilder.loadTexts:h3cDDosAttackEnd.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cAFC':h3cAFC,'h3cAFCLeaf':h3cAFCLeaf,_D:h3cDDosAttackTargetIP,_G:h3cDDosAttackType,_H:h3cDDosAttackPolicy,_I:h3cDDosAttackThreshold,_J:h3cDDosAttackSpeed,'h3cAFCNotify':h3cAFCNotify,'h3cAFCNotifyPrefix':h3cAFCNotifyPrefix,'h3cDDosAttackStart':h3cDDosAttackStart,'h3cDDosAttackEnd':h3cDDosAttackEnd})