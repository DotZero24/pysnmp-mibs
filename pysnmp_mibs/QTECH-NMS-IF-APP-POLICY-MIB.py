_F='read-only'
_E='nmsIfIndex'
_D='QTECH-NMS-IF-APP-POLICY-MIB'
_C='DisplayString'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
nmsMgmt,=mibBuilder.importSymbols('QTECH-NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
_NmsIfAppPolicy_ObjectIdentity=ObjectIdentity
nmsIfAppPolicy=_NmsIfAppPolicy_ObjectIdentity((1,3,6,1,4,1,34751,9,65))
_NmsIfAppPolicyTable_Object=MibTable
nmsIfAppPolicyTable=_NmsIfAppPolicyTable_Object((1,3,6,1,4,1,34751,9,65,1))
if mibBuilder.loadTexts:nmsIfAppPolicyTable.setStatus(_A)
_NmsIfAppPolicyEntry_Object=MibTableRow
nmsIfAppPolicyEntry=_NmsIfAppPolicyEntry_Object((1,3,6,1,4,1,34751,9,65,1,1))
nmsIfAppPolicyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nmsIfAppPolicyEntry.setStatus(_A)
_NmsIfIndex_Type=Integer32
_NmsIfIndex_Object=MibTableColumn
nmsIfIndex=_NmsIfIndex_Object((1,3,6,1,4,1,34751,9,65,1,1,1),_NmsIfIndex_Type())
nmsIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nmsIfIndex.setStatus(_A)
class _NmsIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NmsIfDescr_Type.__name__=_C
_NmsIfDescr_Object=MibTableColumn
nmsIfDescr=_NmsIfDescr_Object((1,3,6,1,4,1,34751,9,65,1,1,2),_NmsIfDescr_Type())
nmsIfDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:nmsIfDescr.setStatus(_A)
_NmsIfInMacACL_Type=DisplayString
_NmsIfInMacACL_Object=MibTableColumn
nmsIfInMacACL=_NmsIfInMacACL_Object((1,3,6,1,4,1,34751,9,65,1,1,3),_NmsIfInMacACL_Type())
nmsIfInMacACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfInMacACL.setStatus(_A)
_NmsIfOutMacACL_Type=DisplayString
_NmsIfOutMacACL_Object=MibTableColumn
nmsIfOutMacACL=_NmsIfOutMacACL_Object((1,3,6,1,4,1,34751,9,65,1,1,4),_NmsIfOutMacACL_Type())
nmsIfOutMacACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfOutMacACL.setStatus(_A)
_NmsIfInIpACL_Type=DisplayString
_NmsIfInIpACL_Object=MibTableColumn
nmsIfInIpACL=_NmsIfInIpACL_Object((1,3,6,1,4,1,34751,9,65,1,1,5),_NmsIfInIpACL_Type())
nmsIfInIpACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfInIpACL.setStatus(_A)
_NmsIfOutIpACL_Type=DisplayString
_NmsIfOutIpACL_Object=MibTableColumn
nmsIfOutIpACL=_NmsIfOutIpACL_Object((1,3,6,1,4,1,34751,9,65,1,1,6),_NmsIfOutIpACL_Type())
nmsIfOutIpACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfOutIpACL.setStatus(_A)
_NmsIfInQosPolicyName_Type=DisplayString
_NmsIfInQosPolicyName_Object=MibTableColumn
nmsIfInQosPolicyName=_NmsIfInQosPolicyName_Object((1,3,6,1,4,1,34751,9,65,1,1,7),_NmsIfInQosPolicyName_Type())
nmsIfInQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfInQosPolicyName.setStatus(_A)
_NmsIfOutQosPolicyName_Type=DisplayString
_NmsIfOutQosPolicyName_Object=MibTableColumn
nmsIfOutQosPolicyName=_NmsIfOutQosPolicyName_Object((1,3,6,1,4,1,34751,9,65,1,1,8),_NmsIfOutQosPolicyName_Type())
nmsIfOutQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsIfOutQosPolicyName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nmsIfAppPolicy':nmsIfAppPolicy,'nmsIfAppPolicyTable':nmsIfAppPolicyTable,'nmsIfAppPolicyEntry':nmsIfAppPolicyEntry,_E:nmsIfIndex,'nmsIfDescr':nmsIfDescr,'nmsIfInMacACL':nmsIfInMacACL,'nmsIfOutMacACL':nmsIfOutMacACL,'nmsIfInIpACL':nmsIfInIpACL,'nmsIfOutIpACL':nmsIfOutIpACL,'nmsIfInQosPolicyName':nmsIfInQosPolicyName,'nmsIfOutQosPolicyName':nmsIfOutQosPolicyName})