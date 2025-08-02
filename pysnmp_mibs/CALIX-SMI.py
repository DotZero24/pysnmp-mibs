_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
calixNetworks=ModuleIdentity((1,3,6,1,4,1,6321))
if mibBuilder.loadTexts:calixNetworks.setRevisions(('2000-08-31 00:26',))
_CalixRegistrations_ObjectIdentity=ObjectIdentity
calixRegistrations=_CalixRegistrations_ObjectIdentity((1,3,6,1,4,1,6321,1))
if mibBuilder.loadTexts:calixRegistrations.setStatus(_A)
_CalixModules_ObjectIdentity=ObjectIdentity
calixModules=_CalixModules_ObjectIdentity((1,3,6,1,4,1,6321,1,1))
if mibBuilder.loadTexts:calixModules.setStatus(_A)
_CalixProducts_ObjectIdentity=ObjectIdentity
calixProducts=_CalixProducts_ObjectIdentity((1,3,6,1,4,1,6321,1,2))
if mibBuilder.loadTexts:calixProducts.setStatus(_A)
_CalixManagement_ObjectIdentity=ObjectIdentity
calixManagement=_CalixManagement_ObjectIdentity((1,3,6,1,4,1,6321,2))
if mibBuilder.loadTexts:calixManagement.setStatus(_A)
mibBuilder.exportSymbols('CALIX-SMI',**{'calixNetworks':calixNetworks,'calixRegistrations':calixRegistrations,'calixModules':calixModules,'calixProducts':calixProducts,'calixManagement':calixManagement})