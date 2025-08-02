_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsdsmon=ModuleIdentity((1,3,6,1,4,1,10876,101,3,4))
if mibBuilder.loadTexts:fsdsmon.setRevisions(('2012-09-05 00:00',))
_FsDsmonTrace_Type=Unsigned32
_FsDsmonTrace_Object=MibScalar
fsDsmonTrace=_FsDsmonTrace_Object((1,3,6,1,4,1,10876,101,3,4,1),_FsDsmonTrace_Type())
fsDsmonTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDsmonTrace.setStatus(_C)
class _FsDsmonAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsDsmonAdminStatus_Type.__name__=_A
_FsDsmonAdminStatus_Object=MibScalar
fsDsmonAdminStatus=_FsDsmonAdminStatus_Object((1,3,6,1,4,1,10876,101,3,4,2),_FsDsmonAdminStatus_Type())
fsDsmonAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDsmonAdminStatus.setStatus(_C)
mibBuilder.exportSymbols('SUPERMICRO-DSMON-MIB',**{'fsdsmon':fsdsmon,'fsDsmonTrace':fsDsmonTrace,'fsDsmonAdminStatus':fsDsmonAdminStatus})