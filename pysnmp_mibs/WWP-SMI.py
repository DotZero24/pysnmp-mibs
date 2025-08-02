_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wwp=ModuleIdentity((1,3,6,1,4,1,6141))
if mibBuilder.loadTexts:wwp.setRevisions(('2013-02-09 01:36',))
_WwpProducts_ObjectIdentity=ObjectIdentity
wwpProducts=_WwpProducts_ObjectIdentity((1,3,6,1,4,1,6141,1))
if mibBuilder.loadTexts:wwpProducts.setStatus(_A)
_WwpModules_ObjectIdentity=ObjectIdentity
wwpModules=_WwpModules_ObjectIdentity((1,3,6,1,4,1,6141,2))
if mibBuilder.loadTexts:wwpModules.setStatus(_A)
_WwpModulesLeos_ObjectIdentity=ObjectIdentity
wwpModulesLeos=_WwpModulesLeos_ObjectIdentity((1,3,6,1,4,1,6141,2,60))
if mibBuilder.loadTexts:wwpModulesLeos.setStatus(_A)
_WwpModulesLeosTce_ObjectIdentity=ObjectIdentity
wwpModulesLeosTce=_WwpModulesLeosTce_ObjectIdentity((1,3,6,1,4,1,6141,2,61))
if mibBuilder.loadTexts:wwpModulesLeosTce.setStatus(_A)
mibBuilder.exportSymbols('WWP-SMI',**{'wwp':wwp,'wwpProducts':wwpProducts,'wwpModules':wwpModules,'wwpModulesLeos':wwpModulesLeos,'wwpModulesLeosTce':wwpModulesLeosTce})