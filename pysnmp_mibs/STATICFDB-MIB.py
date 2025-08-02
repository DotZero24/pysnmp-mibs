_G='swStaticFdbMgmtMacAddr'
_F='swStaticFdbMgmtVlanID'
_E='read-create'
_D='read-only'
_C='STATICFDB-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swStaticFdbMIB=ModuleIdentity((1,3,6,1,4,1,171,12,70))
_SwStaticFdbMgmt_ObjectIdentity=ObjectIdentity
swStaticFdbMgmt=_SwStaticFdbMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,70,1))
_SwStaticFdbMgmtTable_Object=MibTable
swStaticFdbMgmtTable=_SwStaticFdbMgmtTable_Object((1,3,6,1,4,1,171,12,70,1,1))
if mibBuilder.loadTexts:swStaticFdbMgmtTable.setStatus(_A)
_SwStaticFdbMgmtEntry_Object=MibTableRow
swStaticFdbMgmtEntry=_SwStaticFdbMgmtEntry_Object((1,3,6,1,4,1,171,12,70,1,1,1))
swStaticFdbMgmtEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:swStaticFdbMgmtEntry.setStatus(_A)
class _SwStaticFdbMgmtVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwStaticFdbMgmtVlanID_Type.__name__=_B
_SwStaticFdbMgmtVlanID_Object=MibTableColumn
swStaticFdbMgmtVlanID=_SwStaticFdbMgmtVlanID_Object((1,3,6,1,4,1,171,12,70,1,1,1,1),_SwStaticFdbMgmtVlanID_Type())
swStaticFdbMgmtVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:swStaticFdbMgmtVlanID.setStatus(_A)
_SwStaticFdbMgmtMacAddr_Type=MacAddress
_SwStaticFdbMgmtMacAddr_Object=MibTableColumn
swStaticFdbMgmtMacAddr=_SwStaticFdbMgmtMacAddr_Object((1,3,6,1,4,1,171,12,70,1,1,1,2),_SwStaticFdbMgmtMacAddr_Type())
swStaticFdbMgmtMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swStaticFdbMgmtMacAddr.setStatus(_A)
_SwStaticFdbMgmtVlanName_Type=DisplayString
_SwStaticFdbMgmtVlanName_Object=MibTableColumn
swStaticFdbMgmtVlanName=_SwStaticFdbMgmtVlanName_Object((1,3,6,1,4,1,171,12,70,1,1,1,3),_SwStaticFdbMgmtVlanName_Type())
swStaticFdbMgmtVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swStaticFdbMgmtVlanName.setStatus(_A)
class _SwStaticFdbMgmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('self',1),('permanent',2),('permanentdrop',3)))
_SwStaticFdbMgmtType_Type.__name__=_B
_SwStaticFdbMgmtType_Object=MibTableColumn
swStaticFdbMgmtType=_SwStaticFdbMgmtType_Object((1,3,6,1,4,1,171,12,70,1,1,1,4),_SwStaticFdbMgmtType_Type())
swStaticFdbMgmtType.setMaxAccess(_E)
if mibBuilder.loadTexts:swStaticFdbMgmtType.setStatus(_A)
_SwStaticFdbMgmtPortNum_Type=Integer32
_SwStaticFdbMgmtPortNum_Object=MibTableColumn
swStaticFdbMgmtPortNum=_SwStaticFdbMgmtPortNum_Object((1,3,6,1,4,1,171,12,70,1,1,1,5),_SwStaticFdbMgmtPortNum_Type())
swStaticFdbMgmtPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:swStaticFdbMgmtPortNum.setStatus(_A)
_SwStaticFdbMgmtRowStatus_Type=RowStatus
_SwStaticFdbMgmtRowStatus_Object=MibTableColumn
swStaticFdbMgmtRowStatus=_SwStaticFdbMgmtRowStatus_Object((1,3,6,1,4,1,171,12,70,1,1,1,6),_SwStaticFdbMgmtRowStatus_Type())
swStaticFdbMgmtRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swStaticFdbMgmtRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'swStaticFdbMIB':swStaticFdbMIB,'swStaticFdbMgmt':swStaticFdbMgmt,'swStaticFdbMgmtTable':swStaticFdbMgmtTable,'swStaticFdbMgmtEntry':swStaticFdbMgmtEntry,_F:swStaticFdbMgmtVlanID,_G:swStaticFdbMgmtMacAddr,'swStaticFdbMgmtVlanName':swStaticFdbMgmtVlanName,'swStaticFdbMgmtType':swStaticFdbMgmtType,'swStaticFdbMgmtPortNum':swStaticFdbMgmtPortNum,'swStaticFdbMgmtRowStatus':swStaticFdbMgmtRowStatus})