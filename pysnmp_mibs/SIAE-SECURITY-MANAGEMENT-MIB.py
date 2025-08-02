_G='read-create'
_F='serviceIndex'
_E='SIAE-SECURITY-MANAGEMENT-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
securityManagement=ModuleIdentity((1,3,6,1,4,1,3373,1103,82))
if mibBuilder.loadTexts:securityManagement.setRevisions(('2014-04-17 00:00',))
_SecurityManagementMibVersion_Type=Integer32
_SecurityManagementMibVersion_Object=MibScalar
securityManagementMibVersion=_SecurityManagementMibVersion_Object((1,3,6,1,4,1,3373,1103,82,1),_SecurityManagementMibVersion_Type())
securityManagementMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:securityManagementMibVersion.setStatus(_A)
_ServicesTable_Object=MibTable
servicesTable=_ServicesTable_Object((1,3,6,1,4,1,3373,1103,82,2))
if mibBuilder.loadTexts:servicesTable.setStatus(_A)
_ServiceEntry_Object=MibTableRow
serviceEntry=_ServiceEntry_Object((1,3,6,1,4,1,3373,1103,82,2,1))
serviceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:serviceEntry.setStatus(_A)
_ServiceIndex_Type=Integer32
_ServiceIndex_Object=MibTableColumn
serviceIndex=_ServiceIndex_Object((1,3,6,1,4,1,3373,1103,82,2,1,1),_ServiceIndex_Type())
serviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceIndex.setStatus(_A)
class _ServiceName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ServiceName_Type.__name__=_D
_ServiceName_Object=MibTableColumn
serviceName=_ServiceName_Object((1,3,6,1,4,1,3373,1103,82,2,1,2),_ServiceName_Type())
serviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceName.setStatus(_A)
class _ServiceProtocolVersion_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ServiceProtocolVersion_Type.__name__=_D
_ServiceProtocolVersion_Object=MibTableColumn
serviceProtocolVersion=_ServiceProtocolVersion_Object((1,3,6,1,4,1,3373,1103,82,2,1,3),_ServiceProtocolVersion_Type())
serviceProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceProtocolVersion.setStatus(_A)
class _ServiceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_ServiceAdminStatus_Type.__name__=_C
_ServiceAdminStatus_Object=MibTableColumn
serviceAdminStatus=_ServiceAdminStatus_Object((1,3,6,1,4,1,3373,1103,82,2,1,4),_ServiceAdminStatus_Type())
serviceAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:serviceAdminStatus.setStatus(_A)
class _ServiceOperStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notAvailable',0),('running',1),('stopped',2)))
_ServiceOperStatus_Type.__name__=_C
_ServiceOperStatus_Object=MibTableColumn
serviceOperStatus=_ServiceOperStatus_Object((1,3,6,1,4,1,3373,1103,82,2,1,5),_ServiceOperStatus_Type())
serviceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceOperStatus.setStatus(_A)
_ServiceRowStatus_Type=RowStatus
_ServiceRowStatus_Object=MibTableColumn
serviceRowStatus=_ServiceRowStatus_Object((1,3,6,1,4,1,3373,1103,82,2,1,6),_ServiceRowStatus_Type())
serviceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:serviceRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'securityManagement':securityManagement,'securityManagementMibVersion':securityManagementMibVersion,'servicesTable':servicesTable,'serviceEntry':serviceEntry,_F:serviceIndex,'serviceName':serviceName,'serviceProtocolVersion':serviceProtocolVersion,'serviceAdminStatus':serviceAdminStatus,'serviceOperStatus':serviceOperStatus,'serviceRowStatus':serviceRowStatus})