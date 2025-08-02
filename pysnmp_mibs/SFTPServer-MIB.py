_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swSFTPServerMIB=ModuleIdentity((1,3,6,1,4,1,171,12,104))
_SwSFTPServerMgmt_ObjectIdentity=ObjectIdentity
swSFTPServerMgmt=_SwSFTPServerMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,104,1))
_SwSFTPServerVersion_Type=Integer32
_SwSFTPServerVersion_Object=MibScalar
swSFTPServerVersion=_SwSFTPServerVersion_Object((1,3,6,1,4,1,171,12,104,1,1),_SwSFTPServerVersion_Type())
swSFTPServerVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:swSFTPServerVersion.setStatus(_B)
class _SwSFTPServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwSFTPServerState_Type.__name__=_A
_SwSFTPServerState_Object=MibScalar
swSFTPServerState=_SwSFTPServerState_Object((1,3,6,1,4,1,171,12,104,1,2),_SwSFTPServerState_Type())
swSFTPServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSFTPServerState.setStatus(_B)
class _SwSFTPServerConnectionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_SwSFTPServerConnectionTimeout_Type.__name__=_A
_SwSFTPServerConnectionTimeout_Object=MibScalar
swSFTPServerConnectionTimeout=_SwSFTPServerConnectionTimeout_Object((1,3,6,1,4,1,171,12,104,1,3),_SwSFTPServerConnectionTimeout_Type())
swSFTPServerConnectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swSFTPServerConnectionTimeout.setStatus(_B)
mibBuilder.exportSymbols('SFTPServer-MIB',**{'swSFTPServerMIB':swSFTPServerMIB,'swSFTPServerMgmt':swSFTPServerMgmt,'swSFTPServerVersion':swSFTPServerVersion,'swSFTPServerState':swSFTPServerState,'swSFTPServerConnectionTimeout':swSFTPServerConnectionTimeout})