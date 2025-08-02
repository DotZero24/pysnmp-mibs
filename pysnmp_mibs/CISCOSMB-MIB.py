if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cisco=ModuleIdentity((1,3,6,1,4,1,9))
if mibBuilder.loadTexts:cisco.setRevisions(('2010-10-31 00:00',))
_OtherEnterprises_ObjectIdentity=ObjectIdentity
otherEnterprises=_OtherEnterprises_ObjectIdentity((1,3,6,1,4,1,9,6))
_Ciscosb_ObjectIdentity=ObjectIdentity
ciscosb=_Ciscosb_ObjectIdentity((1,3,6,1,4,1,9,6,1))
_Switch001_ObjectIdentity=ObjectIdentity
switch001=_Switch001_ObjectIdentity((1,3,6,1,4,1,9,6,1,101))
_RndMib_ObjectIdentity=ObjectIdentity
rndMib=_RndMib_ObjectIdentity((1,3,6,1,4,1,9,6,1,101))
mibBuilder.exportSymbols('CISCOSMB-MIB',**{'cisco':cisco,'otherEnterprises':otherEnterprises,'ciscosb':ciscosb,'switch001':switch001,'rndMib':rndMib})