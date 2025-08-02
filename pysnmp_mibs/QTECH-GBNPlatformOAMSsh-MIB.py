_C='read-only'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnPlatformOAM,=mibBuilder.importSymbols('QTECH-GBNPlatformOAM-MIB','gbnPlatformOAM')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnPlatformOAMSsh=ModuleIdentity((1,3,6,1,4,1,27514,1,2,1,1,11))
if mibBuilder.loadTexts:gbnPlatformOAMSsh.setRevisions(('1905-05-25 00:00',))
class _SshVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
_SshVersion_Type.__name__=_A
_SshVersion_Object=MibScalar
sshVersion=_SshVersion_Object((1,3,6,1,4,1,27514,1,2,1,1,11,1),_SshVersion_Type())
sshVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sshVersion.setStatus(_B)
class _SshState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SshState_Type.__name__=_A
_SshState_Object=MibScalar
sshState=_SshState_Object((1,3,6,1,4,1,27514,1,2,1,1,11,2),_SshState_Type())
sshState.setMaxAccess('read-write')
if mibBuilder.loadTexts:sshState.setStatus(_B)
class _SshKeyAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('unavailable',2)))
_SshKeyAvailable_Type.__name__=_A
_SshKeyAvailable_Object=MibScalar
sshKeyAvailable=_SshKeyAvailable_Object((1,3,6,1,4,1,27514,1,2,1,1,11,3),_SshKeyAvailable_Type())
sshKeyAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:sshKeyAvailable.setStatus(_B)
mibBuilder.exportSymbols('QTECH-GBNPlatformOAMSsh-MIB',**{'gbnPlatformOAMSsh':gbnPlatformOAMSsh,'sshVersion':sshVersion,'sshState':sshState,'sshKeyAvailable':sshKeyAvailable})