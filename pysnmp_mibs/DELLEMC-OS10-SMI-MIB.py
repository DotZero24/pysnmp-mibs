_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dell=ModuleIdentity((1,3,6,1,4,1,674))
if mibBuilder.loadTexts:dell.setRevisions(('2018-07-06 12:00',))
_EnterpriseSW_ObjectIdentity=ObjectIdentity
enterpriseSW=_EnterpriseSW_ObjectIdentity((1,3,6,1,4,1,674,11000))
_Networking_ObjectIdentity=ObjectIdentity
networking=_Networking_ObjectIdentity((1,3,6,1,4,1,674,11000,5000))
_Os10_ObjectIdentity=ObjectIdentity
os10=_Os10_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100))
if mibBuilder.loadTexts:os10.setStatus(_A)
_Os10Experiment_ObjectIdentity=ObjectIdentity
os10Experiment=_Os10Experiment_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,200))
if mibBuilder.loadTexts:os10Experiment.setStatus(_A)
mibBuilder.exportSymbols('DELLEMC-OS10-SMI-MIB',**{'dell':dell,'enterpriseSW':enterpriseSW,'networking':networking,'os10':os10,'os10Experiment':os10Experiment})