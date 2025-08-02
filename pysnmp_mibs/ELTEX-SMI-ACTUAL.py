_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
eltexLtd=ModuleIdentity((1,3,6,1,4,1,35265))
if mibBuilder.loadTexts:eltexLtd.setRevisions(('2012-05-29 00:00',))
_ElHardware_ObjectIdentity=ObjectIdentity
elHardware=_ElHardware_ObjectIdentity((1,3,6,1,4,1,35265,1))
if mibBuilder.loadTexts:elHardware.setStatus(_A)
_ElSoftware_ObjectIdentity=ObjectIdentity
elSoftware=_ElSoftware_ObjectIdentity((1,3,6,1,4,1,35265,2))
if mibBuilder.loadTexts:elSoftware.setStatus(_A)
_EltrapGroup_ObjectIdentity=ObjectIdentity
eltrapGroup=_EltrapGroup_ObjectIdentity((1,3,6,1,4,1,35265,3))
if mibBuilder.loadTexts:eltrapGroup.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-SMI-ACTUAL',**{'eltexLtd':eltexLtd,'elHardware':elHardware,'elSoftware':elSoftware,'eltrapGroup':eltrapGroup})