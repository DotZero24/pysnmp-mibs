if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2OemMib=ModuleIdentity((1,3,6,1,4,1,248,11,15))
if mibBuilder.loadTexts:hm2OemMib.setRevisions(('2011-03-31 00:00',))
_Hm2OemMibObjects_ObjectIdentity=ObjectIdentity
hm2OemMibObjects=_Hm2OemMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,15,1))
_Hm2OemID_Type=Integer32
_Hm2OemID_Object=MibScalar
hm2OemID=_Hm2OemID_Object((1,3,6,1,4,1,248,11,15,1,1),_Hm2OemID_Type())
hm2OemID.setMaxAccess('read-only')
if mibBuilder.loadTexts:hm2OemID.setStatus('current')
mibBuilder.exportSymbols('HM2-OEM-MIB',**{'hm2OemMib':hm2OemMib,'hm2OemMibObjects':hm2OemMibObjects,'hm2OemID':hm2OemID})