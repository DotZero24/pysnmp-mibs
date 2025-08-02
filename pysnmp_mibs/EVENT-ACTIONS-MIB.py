_O='ctActionExtensionID'
_N='delete'
_M='normal'
_L='DisplayString'
_K='eventIndex'
_J='RMON-MIB'
_I='ctActionObjectBase'
_H='disable'
_G='enable'
_F='EVENT-ACTIONS-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='deprecated'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctActions,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctActions')
eventIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
_CtActionDefn_ObjectIdentity=ObjectIdentity
ctActionDefn=_CtActionDefn_ObjectIdentity((1,3,6,1,4,1,52,4,3,4,1))
_CtEventActionTable_Object=MibTable
ctEventActionTable=_CtEventActionTable_Object((1,3,6,1,4,1,52,4,3,4,1,1))
if mibBuilder.loadTexts:ctEventActionTable.setStatus(_A)
_CtEventActionEntry_Object=MibTableRow
ctEventActionEntry=_CtEventActionEntry_Object((1,3,6,1,4,1,52,4,3,4,1,1,1))
ctEventActionEntry.setIndexNames((0,_J,_K),(0,_F,_I))
if mibBuilder.loadTexts:ctEventActionEntry.setStatus(_A)
_CtActionObjectBase_Type=ObjectIdentifier
_CtActionObjectBase_Object=MibTableColumn
ctActionObjectBase=_CtActionObjectBase_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,1),_CtActionObjectBase_Type())
ctActionObjectBase.setMaxAccess(_D)
if mibBuilder.loadTexts:ctActionObjectBase.setStatus(_A)
_CtActionValue_Type=Integer32
_CtActionValue_Object=MibTableColumn
ctActionValue=_CtActionValue_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,2),_CtActionValue_Type())
ctActionValue.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionValue.setStatus(_A)
class _CtActionOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,4),('error',5),('invalidExtension',6)))
_CtActionOperStatus_Type.__name__=_C
_CtActionOperStatus_Object=MibTableColumn
ctActionOperStatus=_CtActionOperStatus_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,3),_CtActionOperStatus_Type())
ctActionOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctActionOperStatus.setStatus(_A)
class _CtActionAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3)))
_CtActionAdminStatus_Type.__name__=_C
_CtActionAdminStatus_Object=MibTableColumn
ctActionAdminStatus=_CtActionAdminStatus_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,4),_CtActionAdminStatus_Type())
ctActionAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionAdminStatus.setStatus(_A)
class _CtActionDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CtActionDescription_Type.__name__=_L
_CtActionDescription_Object=MibTableColumn
ctActionDescription=_CtActionDescription_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,5),_CtActionDescription_Type())
ctActionDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionDescription.setStatus(_A)
class _CtActionOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtActionOrder_Type.__name__=_C
_CtActionOrder_Object=MibTableColumn
ctActionOrder=_CtActionOrder_Object((1,3,6,1,4,1,52,4,3,4,1,1,1,6),_CtActionOrder_Type())
ctActionOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionOrder.setStatus(_A)
_CtActionExtensionTable_Object=MibTable
ctActionExtensionTable=_CtActionExtensionTable_Object((1,3,6,1,4,1,52,4,3,4,1,2))
if mibBuilder.loadTexts:ctActionExtensionTable.setStatus(_B)
_CtActionExtensionEntry_Object=MibTableRow
ctActionExtensionEntry=_CtActionExtensionEntry_Object((1,3,6,1,4,1,52,4,3,4,1,2,1))
ctActionExtensionEntry.setIndexNames((0,_F,_I),(0,_F,_O))
if mibBuilder.loadTexts:ctActionExtensionEntry.setStatus(_B)
_CtActionExtensionID_Type=Integer32
_CtActionExtensionID_Object=MibTableColumn
ctActionExtensionID=_CtActionExtensionID_Object((1,3,6,1,4,1,52,4,3,4,1,2,1,1),_CtActionExtensionID_Type())
ctActionExtensionID.setMaxAccess(_D)
if mibBuilder.loadTexts:ctActionExtensionID.setStatus(_B)
_CtActionExtensionOID_Type=ObjectIdentifier
_CtActionExtensionOID_Object=MibTableColumn
ctActionExtensionOID=_CtActionExtensionOID_Object((1,3,6,1,4,1,52,4,3,4,1,2,1,2),_CtActionExtensionOID_Type())
ctActionExtensionOID.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionExtensionOID.setStatus(_B)
_CtActionExtensionValue_Type=Integer32
_CtActionExtensionValue_Object=MibTableColumn
ctActionExtensionValue=_CtActionExtensionValue_Object((1,3,6,1,4,1,52,4,3,4,1,2,1,3),_CtActionExtensionValue_Type())
ctActionExtensionValue.setMaxAccess(_D)
if mibBuilder.loadTexts:ctActionExtensionValue.setStatus(_B)
class _CtActionExtensionOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_H,2),(_M,4),('error',5)))
_CtActionExtensionOperStatus_Type.__name__=_C
_CtActionExtensionOperStatus_Object=MibTableColumn
ctActionExtensionOperStatus=_CtActionExtensionOperStatus_Object((1,3,6,1,4,1,52,4,3,4,1,2,1,4),_CtActionExtensionOperStatus_Type())
ctActionExtensionOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctActionExtensionOperStatus.setStatus(_B)
class _CtActionExtensionAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_N,3)))
_CtActionExtensionAdminStatus_Type.__name__=_C
_CtActionExtensionAdminStatus_Object=MibTableColumn
ctActionExtensionAdminStatus=_CtActionExtensionAdminStatus_Object((1,3,6,1,4,1,52,4,3,4,1,2,1,5),_CtActionExtensionAdminStatus_Type())
ctActionExtensionAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctActionExtensionAdminStatus.setStatus(_B)
_CtEventActionTableEntries_Type=Integer32
_CtEventActionTableEntries_Object=MibScalar
ctEventActionTableEntries=_CtEventActionTableEntries_Object((1,3,6,1,4,1,52,4,3,4,1,3),_CtEventActionTableEntries_Type())
ctEventActionTableEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:ctEventActionTableEntries.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ctActionDefn':ctActionDefn,'ctEventActionTable':ctEventActionTable,'ctEventActionEntry':ctEventActionEntry,_I:ctActionObjectBase,'ctActionValue':ctActionValue,'ctActionOperStatus':ctActionOperStatus,'ctActionAdminStatus':ctActionAdminStatus,'ctActionDescription':ctActionDescription,'ctActionOrder':ctActionOrder,'ctActionExtensionTable':ctActionExtensionTable,'ctActionExtensionEntry':ctActionExtensionEntry,_O:ctActionExtensionID,'ctActionExtensionOID':ctActionExtensionOID,'ctActionExtensionValue':ctActionExtensionValue,'ctActionExtensionOperStatus':ctActionExtensionOperStatus,'ctActionExtensionAdminStatus':ctActionExtensionAdminStatus,'ctEventActionTableEntries':ctEventActionTableEntries})