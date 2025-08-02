_F='headerCompressionIndex'
_E='SIAE-HC-MIB'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
headerCompression=ModuleIdentity((1,3,6,1,4,1,3373,1103,79))
if mibBuilder.loadTexts:headerCompression.setRevisions(('2014-10-07 00:00','2014-03-31 00:00'))
_HeaderCompressionMibVersion_Type=Integer32
_HeaderCompressionMibVersion_Object=MibScalar
headerCompressionMibVersion=_HeaderCompressionMibVersion_Object((1,3,6,1,4,1,3373,1103,79,1),_HeaderCompressionMibVersion_Type())
headerCompressionMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:headerCompressionMibVersion.setStatus(_A)
_HeaderCompressionTable_Object=MibTable
headerCompressionTable=_HeaderCompressionTable_Object((1,3,6,1,4,1,3373,1103,79,2))
if mibBuilder.loadTexts:headerCompressionTable.setStatus(_A)
_HeaderCompressionEntry_Object=MibTableRow
headerCompressionEntry=_HeaderCompressionEntry_Object((1,3,6,1,4,1,3373,1103,79,2,1))
headerCompressionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:headerCompressionEntry.setStatus(_A)
_HeaderCompressionIndex_Type=Integer32
_HeaderCompressionIndex_Object=MibTableColumn
headerCompressionIndex=_HeaderCompressionIndex_Object((1,3,6,1,4,1,3373,1103,79,2,1,1),_HeaderCompressionIndex_Type())
headerCompressionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:headerCompressionIndex.setStatus(_A)
class _HeaderCompressionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HeaderCompressionAdminStatus_Type.__name__=_B
_HeaderCompressionAdminStatus_Object=MibTableColumn
headerCompressionAdminStatus=_HeaderCompressionAdminStatus_Object((1,3,6,1,4,1,3373,1103,79,2,1,2),_HeaderCompressionAdminStatus_Type())
headerCompressionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:headerCompressionAdminStatus.setStatus(_A)
class _HeaderCompressionContextDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ctx16bytes',1),('ctx32bytes',2),('ctx64byets',3),('ctx128bytes',4)))
_HeaderCompressionContextDepth_Type.__name__=_B
_HeaderCompressionContextDepth_Object=MibTableColumn
headerCompressionContextDepth=_HeaderCompressionContextDepth_Object((1,3,6,1,4,1,3373,1103,79,2,1,3),_HeaderCompressionContextDepth_Type())
headerCompressionContextDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:headerCompressionContextDepth.setStatus(_A)
class _HeaderCompressionParsingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('semiMpls',2),('semiIPv4IPv6',3)))
_HeaderCompressionParsingMode_Type.__name__=_B
_HeaderCompressionParsingMode_Object=MibTableColumn
headerCompressionParsingMode=_HeaderCompressionParsingMode_Object((1,3,6,1,4,1,3373,1103,79,2,1,4),_HeaderCompressionParsingMode_Type())
headerCompressionParsingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:headerCompressionParsingMode.setStatus(_A)
class _HeaderCompressionTagEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_HeaderCompressionTagEnable_Type.__name__=_B
_HeaderCompressionTagEnable_Object=MibTableColumn
headerCompressionTagEnable=_HeaderCompressionTagEnable_Object((1,3,6,1,4,1,3373,1103,79,2,1,5),_HeaderCompressionTagEnable_Type())
headerCompressionTagEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:headerCompressionTagEnable.setStatus(_A)
_HeaderCompressionRowStatus_Type=RowStatus
_HeaderCompressionRowStatus_Object=MibTableColumn
headerCompressionRowStatus=_HeaderCompressionRowStatus_Object((1,3,6,1,4,1,3373,1103,79,2,1,6),_HeaderCompressionRowStatus_Type())
headerCompressionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:headerCompressionRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'headerCompression':headerCompression,'headerCompressionMibVersion':headerCompressionMibVersion,'headerCompressionTable':headerCompressionTable,'headerCompressionEntry':headerCompressionEntry,_F:headerCompressionIndex,'headerCompressionAdminStatus':headerCompressionAdminStatus,'headerCompressionContextDepth':headerCompressionContextDepth,'headerCompressionParsingMode':headerCompressionParsingMode,'headerCompressionTagEnable':headerCompressionTagEnable,'headerCompressionRowStatus':headerCompressionRowStatus})