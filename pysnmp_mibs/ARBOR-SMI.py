_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arbornetworks=ModuleIdentity((1,3,6,1,4,1,9694))
if mibBuilder.loadTexts:arbornetworks.setRevisions(('2019-11-18 00:00','2019-08-27 00:00','2013-11-14 00:00','2013-08-19 00:00','2011-07-20 00:00','2009-03-30 00:00','2008-11-13 00:00','2005-09-12 00:00'))
class ArborPercentage(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArbornetworksProducts_ObjectIdentity=ObjectIdentity
arbornetworksProducts=_ArbornetworksProducts_ObjectIdentity((1,3,6,1,4,1,9694,1))
if mibBuilder.loadTexts:arbornetworksProducts.setStatus(_A)
_ArborExperimental_ObjectIdentity=ObjectIdentity
arborExperimental=_ArborExperimental_ObjectIdentity((1,3,6,1,4,1,9694,2))
if mibBuilder.loadTexts:arborExperimental.setStatus(_A)
mibBuilder.exportSymbols('ARBOR-SMI',**{'ArborPercentage':ArborPercentage,'arbornetworks':arbornetworks,'arbornetworksProducts':arbornetworksProducts,'arborExperimental':arborExperimental})