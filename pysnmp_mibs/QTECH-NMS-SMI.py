_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nms=ModuleIdentity((1,3,6,1,4,1,34751))
_NmsProducts_ObjectIdentity=ObjectIdentity
nmsProducts=_NmsProducts_ObjectIdentity((1,3,6,1,4,1,34751,1))
if mibBuilder.loadTexts:nmsProducts.setStatus(_A)
_Nmslocal_ObjectIdentity=ObjectIdentity
nmslocal=_Nmslocal_ObjectIdentity((1,3,6,1,4,1,34751,2))
if mibBuilder.loadTexts:nmslocal.setStatus(_A)
_Nmstemporary_ObjectIdentity=ObjectIdentity
nmstemporary=_Nmstemporary_ObjectIdentity((1,3,6,1,4,1,34751,3))
if mibBuilder.loadTexts:nmstemporary.setStatus(_A)
_NmsMgmt_ObjectIdentity=ObjectIdentity
nmsMgmt=_NmsMgmt_ObjectIdentity((1,3,6,1,4,1,34751,9))
if mibBuilder.loadTexts:nmsMgmt.setStatus(_A)
_NmsModules_ObjectIdentity=ObjectIdentity
nmsModules=_NmsModules_ObjectIdentity((1,3,6,1,4,1,34751,12))
if mibBuilder.loadTexts:nmsModules.setStatus(_A)
_NmsPolicyAuto_ObjectIdentity=ObjectIdentity
nmsPolicyAuto=_NmsPolicyAuto_ObjectIdentity((1,3,6,1,4,1,34751,18))
if mibBuilder.loadTexts:nmsPolicyAuto.setStatus(_A)
_NmsPibToMib_ObjectIdentity=ObjectIdentity
nmsPibToMib=_NmsPibToMib_ObjectIdentity((1,3,6,1,4,1,34751,18,2))
if mibBuilder.loadTexts:nmsPibToMib.setStatus(_A)
_NmsWorkGroup_ObjectIdentity=ObjectIdentity
nmsWorkGroup=_NmsWorkGroup_ObjectIdentity((1,3,6,1,4,1,34751,20))
if mibBuilder.loadTexts:nmsWorkGroup.setStatus(_A)
_NmsEPONGroup_ObjectIdentity=ObjectIdentity
nmsEPONGroup=_NmsEPONGroup_ObjectIdentity((1,3,6,1,4,1,34751,101))
if mibBuilder.loadTexts:nmsEPONGroup.setStatus(_A)
_NmsPTNGroup_ObjectIdentity=ObjectIdentity
nmsPTNGroup=_NmsPTNGroup_ObjectIdentity((1,3,6,1,4,1,34751,102))
if mibBuilder.loadTexts:nmsPTNGroup.setStatus(_A)
mibBuilder.exportSymbols('QTECH-NMS-SMI',**{'nms':nms,'nmsProducts':nmsProducts,'nmslocal':nmslocal,'nmstemporary':nmstemporary,'nmsMgmt':nmsMgmt,'nmsModules':nmsModules,'nmsPolicyAuto':nmsPolicyAuto,'nmsPibToMib':nmsPibToMib,'nmsWorkGroup':nmsWorkGroup,'nmsEPONGroup':nmsEPONGroup,'nmsPTNGroup':nmsPTNGroup})