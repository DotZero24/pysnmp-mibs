_E='rlInventoryEntUnitIfindexID'
_D='rlInventoryEntUnitOrIfindex'
_C='CISCOSB-RLINVENTORYENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class UnitIfindexType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unit',0),('ifindex',1)))
_RlInventoryEntTable_Object=MibTable
rlInventoryEntTable=_RlInventoryEntTable_Object((1,3,6,1,4,1,9,6,1,101,217))
if mibBuilder.loadTexts:rlInventoryEntTable.setStatus(_A)
_RlInventoryEntEntry_Object=MibTableRow
rlInventoryEntEntry=_RlInventoryEntEntry_Object((1,3,6,1,4,1,9,6,1,101,217,1))
rlInventoryEntEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:rlInventoryEntEntry.setStatus(_A)
_RlInventoryEntUnitOrIfindex_Type=UnitIfindexType
_RlInventoryEntUnitOrIfindex_Object=MibTableColumn
rlInventoryEntUnitOrIfindex=_RlInventoryEntUnitOrIfindex_Object((1,3,6,1,4,1,9,6,1,101,217,1,1),_RlInventoryEntUnitOrIfindex_Type())
rlInventoryEntUnitOrIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntUnitOrIfindex.setStatus(_A)
_RlInventoryEntUnitIfindexID_Type=Unsigned32
_RlInventoryEntUnitIfindexID_Object=MibTableColumn
rlInventoryEntUnitIfindexID=_RlInventoryEntUnitIfindexID_Object((1,3,6,1,4,1,9,6,1,101,217,1,2),_RlInventoryEntUnitIfindexID_Type())
rlInventoryEntUnitIfindexID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntUnitIfindexID.setStatus(_A)
_RlInventoryEntVendorID_Type=DisplayString
_RlInventoryEntVendorID_Object=MibTableColumn
rlInventoryEntVendorID=_RlInventoryEntVendorID_Object((1,3,6,1,4,1,9,6,1,101,217,1,3),_RlInventoryEntVendorID_Type())
rlInventoryEntVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntVendorID.setStatus(_A)
_RlInventoryEntPID_Type=DisplayString
_RlInventoryEntPID_Object=MibTableColumn
rlInventoryEntPID=_RlInventoryEntPID_Object((1,3,6,1,4,1,9,6,1,101,217,1,4),_RlInventoryEntPID_Type())
rlInventoryEntPID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntPID.setStatus(_A)
_RlInventoryEntName_Type=DisplayString
_RlInventoryEntName_Object=MibTableColumn
rlInventoryEntName=_RlInventoryEntName_Object((1,3,6,1,4,1,9,6,1,101,217,1,5),_RlInventoryEntName_Type())
rlInventoryEntName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntName.setStatus(_A)
_RlInventoryEntDescription_Type=DisplayString
_RlInventoryEntDescription_Object=MibTableColumn
rlInventoryEntDescription=_RlInventoryEntDescription_Object((1,3,6,1,4,1,9,6,1,101,217,1,6),_RlInventoryEntDescription_Type())
rlInventoryEntDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntDescription.setStatus(_A)
_RlInventoryEntSerialNumber_Type=DisplayString
_RlInventoryEntSerialNumber_Object=MibTableColumn
rlInventoryEntSerialNumber=_RlInventoryEntSerialNumber_Object((1,3,6,1,4,1,9,6,1,101,217,1,7),_RlInventoryEntSerialNumber_Type())
rlInventoryEntSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntSerialNumber.setStatus(_A)
_RlInventoryEntUnitNum_Type=Unsigned32
_RlInventoryEntUnitNum_Object=MibTableColumn
rlInventoryEntUnitNum=_RlInventoryEntUnitNum_Object((1,3,6,1,4,1,9,6,1,101,217,1,8),_RlInventoryEntUnitNum_Type())
rlInventoryEntUnitNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlInventoryEntUnitNum.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'UnitIfindexType':UnitIfindexType,'rlInventoryEntTable':rlInventoryEntTable,'rlInventoryEntEntry':rlInventoryEntEntry,_D:rlInventoryEntUnitOrIfindex,_E:rlInventoryEntUnitIfindexID,'rlInventoryEntVendorID':rlInventoryEntVendorID,'rlInventoryEntPID':rlInventoryEntPID,'rlInventoryEntName':rlInventoryEntName,'rlInventoryEntDescription':rlInventoryEntDescription,'rlInventoryEntSerialNumber':rlInventoryEntSerialNumber,'rlInventoryEntUnitNum':rlInventoryEntUnitNum})