_G='read-only'
_F='nmsOnuUniIfIndex'
_E='NMS-EPON-ONU-UNI-IF-ACL-APP-MIB'
_D='NMS-EPON-LLID'
_C='llidIfIndex'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
llidIfIndex,=mibBuilder.importSymbols(_D,_C)
nmsEPONGroup,=mibBuilder.importSymbols('NMS-SMI','nmsEPONGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_NmsEponOnuUniIfAppPolicy_ObjectIdentity=ObjectIdentity
nmsEponOnuUniIfAppPolicy=_NmsEponOnuUniIfAppPolicy_ObjectIdentity((1,3,6,1,4,1,3320,101,105))
_NmsEponOnuUniIfAppPolicyTable_Object=MibTable
nmsEponOnuUniIfAppPolicyTable=_NmsEponOnuUniIfAppPolicyTable_Object((1,3,6,1,4,1,3320,101,105,1))
if mibBuilder.loadTexts:nmsEponOnuUniIfAppPolicyTable.setStatus(_A)
_NmsEponOnuUniIfAppPolicyEntry_Object=MibTableRow
nmsEponOnuUniIfAppPolicyEntry=_NmsEponOnuUniIfAppPolicyEntry_Object((1,3,6,1,4,1,3320,101,105,1,1))
nmsEponOnuUniIfAppPolicyEntry.setIndexNames((0,_D,_C),(0,_E,_F))
if mibBuilder.loadTexts:nmsEponOnuUniIfAppPolicyEntry.setStatus(_A)
_LlidIfIndex_Type=Integer32
_LlidIfIndex_Object=MibTableColumn
llidIfIndex=_LlidIfIndex_Object((1,3,6,1,4,1,3320,101,105,1,1,1),_LlidIfIndex_Type())
llidIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:llidIfIndex.setStatus(_A)
_NmsOnuUniIfIndex_Type=Integer32
_NmsOnuUniIfIndex_Object=MibTableColumn
nmsOnuUniIfIndex=_NmsOnuUniIfIndex_Object((1,3,6,1,4,1,3320,101,105,1,1,2),_NmsOnuUniIfIndex_Type())
nmsOnuUniIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nmsOnuUniIfIndex.setStatus(_A)
_NmsOnuUniIfInMacACL_Type=DisplayString
_NmsOnuUniIfInMacACL_Object=MibTableColumn
nmsOnuUniIfInMacACL=_NmsOnuUniIfInMacACL_Object((1,3,6,1,4,1,3320,101,105,1,1,3),_NmsOnuUniIfInMacACL_Type())
nmsOnuUniIfInMacACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsOnuUniIfInMacACL.setStatus(_A)
_NmsOnuUniIfOutMacACL_Type=DisplayString
_NmsOnuUniIfOutMacACL_Object=MibTableColumn
nmsOnuUniIfOutMacACL=_NmsOnuUniIfOutMacACL_Object((1,3,6,1,4,1,3320,101,105,1,1,4),_NmsOnuUniIfOutMacACL_Type())
nmsOnuUniIfOutMacACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsOnuUniIfOutMacACL.setStatus(_A)
_NmsOnuUniIfInIpACL_Type=DisplayString
_NmsOnuUniIfInIpACL_Object=MibTableColumn
nmsOnuUniIfInIpACL=_NmsOnuUniIfInIpACL_Object((1,3,6,1,4,1,3320,101,105,1,1,5),_NmsOnuUniIfInIpACL_Type())
nmsOnuUniIfInIpACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsOnuUniIfInIpACL.setStatus(_A)
_NmsOnuUniIfOutIpACL_Type=DisplayString
_NmsOnuUniIfOutIpACL_Object=MibTableColumn
nmsOnuUniIfOutIpACL=_NmsOnuUniIfOutIpACL_Object((1,3,6,1,4,1,3320,101,105,1,1,6),_NmsOnuUniIfOutIpACL_Type())
nmsOnuUniIfOutIpACL.setMaxAccess(_B)
if mibBuilder.loadTexts:nmsOnuUniIfOutIpACL.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nmsEponOnuUniIfAppPolicy':nmsEponOnuUniIfAppPolicy,'nmsEponOnuUniIfAppPolicyTable':nmsEponOnuUniIfAppPolicyTable,'nmsEponOnuUniIfAppPolicyEntry':nmsEponOnuUniIfAppPolicyEntry,_C:llidIfIndex,_F:nmsOnuUniIfIndex,'nmsOnuUniIfInMacACL':nmsOnuUniIfInMacACL,'nmsOnuUniIfOutMacACL':nmsOnuUniIfOutMacACL,'nmsOnuUniIfInIpACL':nmsOnuUniIfInIpACL,'nmsOnuUniIfOutIpACL':nmsOnuUniIfOutIpACL})