_K='rcApplyQoSPolicyInterfacename'
_J='rcQoSPolicyMapClassName'
_I='rcQoSPolicyMapname'
_H='rcQoSClassMapMatchACL'
_G='rcQoSClassMapname'
_F='Unsigned32'
_E='read-create'
_D='not-accessible'
_C='RC-QosPolicy-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rc,=mibBuilder.importSymbols('RC-SMI','rc')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'MacAddress','PhysAddress','RowStatus','TextualConvention')
rcQoSPolicy=ModuleIdentity((1,3,6,1,4,1,65000,3))
if mibBuilder.loadTexts:rcQoSPolicy.setRevisions(('2015-03-11 00:00',))
_RcQoSClassMapTable_Object=MibTable
rcQoSClassMapTable=_RcQoSClassMapTable_Object((1,3,6,1,4,1,65000,3,1))
if mibBuilder.loadTexts:rcQoSClassMapTable.setStatus(_A)
_RcQoSClassMapEntry_Object=MibTableRow
rcQoSClassMapEntry=_RcQoSClassMapEntry_Object((1,3,6,1,4,1,65000,3,1,1))
rcQoSClassMapEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:rcQoSClassMapEntry.setStatus(_A)
class _RcQoSClassMapname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcQoSClassMapname_Type.__name__=_B
_RcQoSClassMapname_Object=MibTableColumn
rcQoSClassMapname=_RcQoSClassMapname_Object((1,3,6,1,4,1,65000,3,1,1,1),_RcQoSClassMapname_Type())
rcQoSClassMapname.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQoSClassMapname.setStatus(_A)
class _RcQoSClassMapMatchACL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcQoSClassMapMatchACL_Type.__name__=_B
_RcQoSClassMapMatchACL_Object=MibTableColumn
rcQoSClassMapMatchACL=_RcQoSClassMapMatchACL_Object((1,3,6,1,4,1,65000,3,1,1,2),_RcQoSClassMapMatchACL_Type())
rcQoSClassMapMatchACL.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQoSClassMapMatchACL.setStatus(_A)
_RcQoSClassMapRowSta_Type=RowStatus
_RcQoSClassMapRowSta_Object=MibTableColumn
rcQoSClassMapRowSta=_RcQoSClassMapRowSta_Object((1,3,6,1,4,1,65000,3,1,1,3),_RcQoSClassMapRowSta_Type())
rcQoSClassMapRowSta.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQoSClassMapRowSta.setStatus(_A)
_RcQoSPolicyMapTable_Object=MibTable
rcQoSPolicyMapTable=_RcQoSPolicyMapTable_Object((1,3,6,1,4,1,65000,3,2))
if mibBuilder.loadTexts:rcQoSPolicyMapTable.setStatus(_A)
_RcQoSPolicyMapEntry_Object=MibTableRow
rcQoSPolicyMapEntry=_RcQoSPolicyMapEntry_Object((1,3,6,1,4,1,65000,3,2,1))
rcQoSPolicyMapEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:rcQoSPolicyMapEntry.setStatus(_A)
class _RcQoSPolicyMapname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcQoSPolicyMapname_Type.__name__=_B
_RcQoSPolicyMapname_Object=MibTableColumn
rcQoSPolicyMapname=_RcQoSPolicyMapname_Object((1,3,6,1,4,1,65000,3,2,1,1),_RcQoSPolicyMapname_Type())
rcQoSPolicyMapname.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQoSPolicyMapname.setStatus(_A)
class _RcQoSPolicyMapClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcQoSPolicyMapClassName_Type.__name__=_B
_RcQoSPolicyMapClassName_Object=MibTableColumn
rcQoSPolicyMapClassName=_RcQoSPolicyMapClassName_Object((1,3,6,1,4,1,65000,3,2,1,2),_RcQoSPolicyMapClassName_Type())
rcQoSPolicyMapClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:rcQoSPolicyMapClassName.setStatus(_A)
class _RcQoSPolicyMapSetIPDSCP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQoSPolicyMapSetIPDSCP_Type.__name__=_F
_RcQoSPolicyMapSetIPDSCP_Object=MibTableColumn
rcQoSPolicyMapSetIPDSCP=_RcQoSPolicyMapSetIPDSCP_Object((1,3,6,1,4,1,65000,3,2,1,3),_RcQoSPolicyMapSetIPDSCP_Type())
rcQoSPolicyMapSetIPDSCP.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQoSPolicyMapSetIPDSCP.setStatus(_A)
_RcQoSPolicyMapRowSta_Type=RowStatus
_RcQoSPolicyMapRowSta_Object=MibTableColumn
rcQoSPolicyMapRowSta=_RcQoSPolicyMapRowSta_Object((1,3,6,1,4,1,65000,3,2,1,4),_RcQoSPolicyMapRowSta_Type())
rcQoSPolicyMapRowSta.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQoSPolicyMapRowSta.setStatus(_A)
_RcApplyQoSPolicyMapTable_Object=MibTable
rcApplyQoSPolicyMapTable=_RcApplyQoSPolicyMapTable_Object((1,3,6,1,4,1,65000,3,3))
if mibBuilder.loadTexts:rcApplyQoSPolicyMapTable.setStatus(_A)
_RcApplyQoSPolicyMapEntry_Object=MibTableRow
rcApplyQoSPolicyMapEntry=_RcApplyQoSPolicyMapEntry_Object((1,3,6,1,4,1,65000,3,3,1))
rcApplyQoSPolicyMapEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:rcApplyQoSPolicyMapEntry.setStatus(_A)
class _RcApplyQoSPolicyInterfacename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcApplyQoSPolicyInterfacename_Type.__name__=_B
_RcApplyQoSPolicyInterfacename_Object=MibTableColumn
rcApplyQoSPolicyInterfacename=_RcApplyQoSPolicyInterfacename_Object((1,3,6,1,4,1,65000,3,3,1,1),_RcApplyQoSPolicyInterfacename_Type())
rcApplyQoSPolicyInterfacename.setMaxAccess(_D)
if mibBuilder.loadTexts:rcApplyQoSPolicyInterfacename.setStatus(_A)
class _RcApplyQoSPolicyMapname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_RcApplyQoSPolicyMapname_Type.__name__=_B
_RcApplyQoSPolicyMapname_Object=MibTableColumn
rcApplyQoSPolicyMapname=_RcApplyQoSPolicyMapname_Object((1,3,6,1,4,1,65000,3,3,1,2),_RcApplyQoSPolicyMapname_Type())
rcApplyQoSPolicyMapname.setMaxAccess(_E)
if mibBuilder.loadTexts:rcApplyQoSPolicyMapname.setStatus(_A)
_RcApplyQoSPolicyMapRowSta_Type=RowStatus
_RcApplyQoSPolicyMapRowSta_Object=MibTableColumn
rcApplyQoSPolicyMapRowSta=_RcApplyQoSPolicyMapRowSta_Object((1,3,6,1,4,1,65000,3,3,1,3),_RcApplyQoSPolicyMapRowSta_Type())
rcApplyQoSPolicyMapRowSta.setMaxAccess(_E)
if mibBuilder.loadTexts:rcApplyQoSPolicyMapRowSta.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcQoSPolicy':rcQoSPolicy,'rcQoSClassMapTable':rcQoSClassMapTable,'rcQoSClassMapEntry':rcQoSClassMapEntry,_G:rcQoSClassMapname,_H:rcQoSClassMapMatchACL,'rcQoSClassMapRowSta':rcQoSClassMapRowSta,'rcQoSPolicyMapTable':rcQoSPolicyMapTable,'rcQoSPolicyMapEntry':rcQoSPolicyMapEntry,_I:rcQoSPolicyMapname,_J:rcQoSPolicyMapClassName,'rcQoSPolicyMapSetIPDSCP':rcQoSPolicyMapSetIPDSCP,'rcQoSPolicyMapRowSta':rcQoSPolicyMapRowSta,'rcApplyQoSPolicyMapTable':rcApplyQoSPolicyMapTable,'rcApplyQoSPolicyMapEntry':rcApplyQoSPolicyMapEntry,_K:rcApplyQoSPolicyInterfacename,'rcApplyQoSPolicyMapname':rcApplyQoSPolicyMapname,'rcApplyQoSPolicyMapRowSta':rcApplyQoSPolicyMapRowSta})