_H='remoteElementIpAddress'
_G='SIAE-RET-MIB'
_F='DisplayString'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
remElement=ModuleIdentity((1,3,6,1,4,1,3373,1103,70))
if mibBuilder.loadTexts:remElement.setRevisions(('2014-06-23 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _RemoteElementMibVersion_Type(Integer32):defaultValue=1
_RemoteElementMibVersion_Type.__name__=_C
_RemoteElementMibVersion_Object=MibScalar
remoteElementMibVersion=_RemoteElementMibVersion_Object((1,3,6,1,4,1,3373,1103,70,1),_RemoteElementMibVersion_Type())
remoteElementMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteElementMibVersion.setStatus(_A)
_RemoteElementTable_Object=MibTable
remoteElementTable=_RemoteElementTable_Object((1,3,6,1,4,1,3373,1103,70,2))
if mibBuilder.loadTexts:remoteElementTable.setStatus(_A)
_RemoteElementEntry_Object=MibTableRow
remoteElementEntry=_RemoteElementEntry_Object((1,3,6,1,4,1,3373,1103,70,2,1))
remoteElementEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:remoteElementEntry.setStatus(_A)
_RemoteElementIpAddress_Type=IpAddress
_RemoteElementIpAddress_Object=MibTableColumn
remoteElementIpAddress=_RemoteElementIpAddress_Object((1,3,6,1,4,1,3373,1103,70,2,1,1),_RemoteElementIpAddress_Type())
remoteElementIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteElementIpAddress.setStatus(_A)
class _RemoteElementGosipAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RemoteElementGosipAddress_Type.__name__=_E
_RemoteElementGosipAddress_Object=MibTableColumn
remoteElementGosipAddress=_RemoteElementGosipAddress_Object((1,3,6,1,4,1,3373,1103,70,2,1,2),_RemoteElementGosipAddress_Type())
remoteElementGosipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteElementGosipAddress.setStatus(_A)
class _RemoteElementLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RemoteElementLabel_Type.__name__=_F
_RemoteElementLabel_Object=MibTableColumn
remoteElementLabel=_RemoteElementLabel_Object((1,3,6,1,4,1,3373,1103,70,2,1,3),_RemoteElementLabel_Type())
remoteElementLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteElementLabel.setStatus(_A)
class _RemoteElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('elemManager',1),('external',2),('remote',3),('snm',4)))
_RemoteElementType_Type.__name__=_C
_RemoteElementType_Object=MibTableColumn
remoteElementType=_RemoteElementType_Object((1,3,6,1,4,1,3373,1103,70,2,1,4),_RemoteElementType_Type())
remoteElementType.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteElementType.setStatus(_A)
_RemoteElementRadioBranchId_Type=Integer32
_RemoteElementRadioBranchId_Object=MibTableColumn
remoteElementRadioBranchId=_RemoteElementRadioBranchId_Object((1,3,6,1,4,1,3373,1103,70,2,1,5),_RemoteElementRadioBranchId_Type())
remoteElementRadioBranchId.setMaxAccess(_D)
if mibBuilder.loadTexts:remoteElementRadioBranchId.setStatus(_A)
_RemoteElementRowStatus_Type=RowStatus
_RemoteElementRowStatus_Object=MibTableColumn
remoteElementRowStatus=_RemoteElementRowStatus_Object((1,3,6,1,4,1,3373,1103,70,2,1,6),_RemoteElementRowStatus_Type())
remoteElementRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteElementRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'remElement':remElement,'remoteElementMibVersion':remoteElementMibVersion,'remoteElementTable':remoteElementTable,'remoteElementEntry':remoteElementEntry,_H:remoteElementIpAddress,'remoteElementGosipAddress':remoteElementGosipAddress,'remoteElementLabel':remoteElementLabel,'remoteElementType':remoteElementType,'remoteElementRadioBranchId':remoteElementRadioBranchId,'remoteElementRowStatus':remoteElementRowStatus})