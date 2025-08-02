_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlCDB=ModuleIdentity((1,3,6,1,4,1,4526,17,94))
if mibBuilder.loadTexts:rlCDB.setRevisions(('2007-01-02 00:00',))
_RlStartupCDBChanged_Type=TruthValue
_RlStartupCDBChanged_Object=MibScalar
rlStartupCDBChanged=_RlStartupCDBChanged_Object((1,3,6,1,4,1,4526,17,94,1),_RlStartupCDBChanged_Type())
rlStartupCDBChanged.setMaxAccess(_A)
if mibBuilder.loadTexts:rlStartupCDBChanged.setStatus(_B)
_RlManualReboot_Type=TruthValue
_RlManualReboot_Object=MibScalar
rlManualReboot=_RlManualReboot_Object((1,3,6,1,4,1,4526,17,94,2),_RlManualReboot_Type())
rlManualReboot.setMaxAccess(_A)
if mibBuilder.loadTexts:rlManualReboot.setStatus(_B)
_RlStartupCDBEmpty_Type=TruthValue
_RlStartupCDBEmpty_Object=MibScalar
rlStartupCDBEmpty=_RlStartupCDBEmpty_Object((1,3,6,1,4,1,4526,17,94,3),_RlStartupCDBEmpty_Type())
rlStartupCDBEmpty.setMaxAccess(_A)
if mibBuilder.loadTexts:rlStartupCDBEmpty.setStatus(_B)
mibBuilder.exportSymbols('NETGEAR-RADLAN-CDB-MIB',**{'rlCDB':rlCDB,'rlStartupCDBChanged':rlStartupCDBChanged,'rlManualReboot':rlManualReboot,'rlStartupCDBEmpty':rlStartupCDBEmpty})