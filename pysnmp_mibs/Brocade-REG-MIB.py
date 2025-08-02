_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bcsi=ModuleIdentity((1,3,6,1,4,1,1588))
if mibBuilder.loadTexts:bcsi.setRevisions(('2012-02-03 00:00',))
_CommDev_ObjectIdentity=ObjectIdentity
commDev=_CommDev_ObjectIdentity((1,3,6,1,4,1,1588,2))
if mibBuilder.loadTexts:commDev.setStatus(_A)
_Fibrechannel_ObjectIdentity=ObjectIdentity
fibrechannel=_Fibrechannel_ObjectIdentity((1,3,6,1,4,1,1588,2,1))
if mibBuilder.loadTexts:fibrechannel.setStatus(_A)
_FcSwitch_ObjectIdentity=ObjectIdentity
fcSwitch=_FcSwitch_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1))
if mibBuilder.loadTexts:fcSwitch.setStatus(_A)
_Nos_ObjectIdentity=ObjectIdentity
nos=_Nos_ObjectIdentity((1,3,6,1,4,1,1588,2,2))
if mibBuilder.loadTexts:nos.setStatus(_A)
_BcsiReg_ObjectIdentity=ObjectIdentity
bcsiReg=_BcsiReg_ObjectIdentity((1,3,6,1,4,1,1588,3))
if mibBuilder.loadTexts:bcsiReg.setStatus(_A)
_BcsiModules_ObjectIdentity=ObjectIdentity
bcsiModules=_BcsiModules_ObjectIdentity((1,3,6,1,4,1,1588,3,1))
if mibBuilder.loadTexts:bcsiModules.setStatus(_A)
_BrocadeAgentCapability_ObjectIdentity=ObjectIdentity
brocadeAgentCapability=_BrocadeAgentCapability_ObjectIdentity((1,3,6,1,4,1,1588,3,2))
if mibBuilder.loadTexts:brocadeAgentCapability.setStatus(_A)
mibBuilder.exportSymbols('Brocade-REG-MIB',**{'bcsi':bcsi,'commDev':commDev,'fibrechannel':fibrechannel,'fcSwitch':fcSwitch,'nos':nos,'bcsiReg':bcsiReg,'bcsiModules':bcsiModules,'brocadeAgentCapability':brocadeAgentCapability})