_M='aristaTapaggPolicyGroup'
_L='aristaTapaggPolicyBytesMatched'
_K='aristaTapaggPolicyPktsMatched'
_J='aristaTapaggPolicyClassName'
_I='aristaTapaggPolicyName'
_H='aristaTapaggPolicyClassIndex'
_G='not-accessible'
_F='Integer32'
_E='aristaTapaggPolicyId'
_D='DisplayString'
_C='read-only'
_B='ARISTA-TAPAGG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AristaQosShortId,=mibBuilder.importSymbols('ARISTA-QOS-MIB','AristaQosShortId')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
aristaTapaggMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,31))
if mibBuilder.loadTexts:aristaTapaggMIB.setRevisions(('2021-04-23 00:00',))
_AristaTapaggMibObjects_ObjectIdentity=ObjectIdentity
aristaTapaggMibObjects=_AristaTapaggMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,31,1))
_AristaTapaggPolicyTable_Object=MibTable
aristaTapaggPolicyTable=_AristaTapaggPolicyTable_Object((1,3,6,1,4,1,30065,3,31,1,1))
if mibBuilder.loadTexts:aristaTapaggPolicyTable.setStatus(_A)
_AristaTapaggPolicyEntry_Object=MibTableRow
aristaTapaggPolicyEntry=_AristaTapaggPolicyEntry_Object((1,3,6,1,4,1,30065,3,31,1,1,1))
aristaTapaggPolicyEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:aristaTapaggPolicyEntry.setStatus(_A)
_AristaTapaggPolicyId_Type=AristaQosShortId
_AristaTapaggPolicyId_Object=MibTableColumn
aristaTapaggPolicyId=_AristaTapaggPolicyId_Object((1,3,6,1,4,1,30065,3,31,1,1,1,1),_AristaTapaggPolicyId_Type())
aristaTapaggPolicyId.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaTapaggPolicyId.setStatus(_A)
class _AristaTapaggPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaTapaggPolicyName_Type.__name__=_D
_AristaTapaggPolicyName_Object=MibTableColumn
aristaTapaggPolicyName=_AristaTapaggPolicyName_Object((1,3,6,1,4,1,30065,3,31,1,1,1,2),_AristaTapaggPolicyName_Type())
aristaTapaggPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaTapaggPolicyName.setStatus(_A)
_AristaTapaggPolicyClassTable_Object=MibTable
aristaTapaggPolicyClassTable=_AristaTapaggPolicyClassTable_Object((1,3,6,1,4,1,30065,3,31,1,2))
if mibBuilder.loadTexts:aristaTapaggPolicyClassTable.setStatus(_A)
_AristaTapaggPolicyClassEntry_Object=MibTableRow
aristaTapaggPolicyClassEntry=_AristaTapaggPolicyClassEntry_Object((1,3,6,1,4,1,30065,3,31,1,2,1))
aristaTapaggPolicyClassEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:aristaTapaggPolicyClassEntry.setStatus(_A)
class _AristaTapaggPolicyClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AristaTapaggPolicyClassIndex_Type.__name__=_F
_AristaTapaggPolicyClassIndex_Object=MibTableColumn
aristaTapaggPolicyClassIndex=_AristaTapaggPolicyClassIndex_Object((1,3,6,1,4,1,30065,3,31,1,2,1,1),_AristaTapaggPolicyClassIndex_Type())
aristaTapaggPolicyClassIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaTapaggPolicyClassIndex.setStatus(_A)
class _AristaTapaggPolicyClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaTapaggPolicyClassName_Type.__name__=_D
_AristaTapaggPolicyClassName_Object=MibTableColumn
aristaTapaggPolicyClassName=_AristaTapaggPolicyClassName_Object((1,3,6,1,4,1,30065,3,31,1,2,1,2),_AristaTapaggPolicyClassName_Type())
aristaTapaggPolicyClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaTapaggPolicyClassName.setStatus(_A)
_AristaTapaggPolicyPktsMatched_Type=Counter64
_AristaTapaggPolicyPktsMatched_Object=MibTableColumn
aristaTapaggPolicyPktsMatched=_AristaTapaggPolicyPktsMatched_Object((1,3,6,1,4,1,30065,3,31,1,2,1,3),_AristaTapaggPolicyPktsMatched_Type())
aristaTapaggPolicyPktsMatched.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaTapaggPolicyPktsMatched.setStatus(_A)
_AristaTapaggPolicyBytesMatched_Type=Counter64
_AristaTapaggPolicyBytesMatched_Object=MibTableColumn
aristaTapaggPolicyBytesMatched=_AristaTapaggPolicyBytesMatched_Object((1,3,6,1,4,1,30065,3,31,1,2,1,4),_AristaTapaggPolicyBytesMatched_Type())
aristaTapaggPolicyBytesMatched.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaTapaggPolicyBytesMatched.setStatus(_A)
_AristaTapaggMibConformance_ObjectIdentity=ObjectIdentity
aristaTapaggMibConformance=_AristaTapaggMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,31,2))
_AristaTapaggMibCompliances_ObjectIdentity=ObjectIdentity
aristaTapaggMibCompliances=_AristaTapaggMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,31,2,1))
_AristaTapaggMibGroups_ObjectIdentity=ObjectIdentity
aristaTapaggMibGroups=_AristaTapaggMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,31,2,2))
aristaTapaggPolicyGroup=ObjectGroup((1,3,6,1,4,1,30065,3,31,2,2,1))
aristaTapaggPolicyGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:aristaTapaggPolicyGroup.setStatus(_A)
aristaTapaggMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,31,2,1,1))
aristaTapaggMibCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:aristaTapaggMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaTapaggMIB':aristaTapaggMIB,'aristaTapaggMibObjects':aristaTapaggMibObjects,'aristaTapaggPolicyTable':aristaTapaggPolicyTable,'aristaTapaggPolicyEntry':aristaTapaggPolicyEntry,_E:aristaTapaggPolicyId,_I:aristaTapaggPolicyName,'aristaTapaggPolicyClassTable':aristaTapaggPolicyClassTable,'aristaTapaggPolicyClassEntry':aristaTapaggPolicyClassEntry,_H:aristaTapaggPolicyClassIndex,_J:aristaTapaggPolicyClassName,_K:aristaTapaggPolicyPktsMatched,_L:aristaTapaggPolicyBytesMatched,'aristaTapaggMibConformance':aristaTapaggMibConformance,'aristaTapaggMibCompliances':aristaTapaggMibCompliances,'aristaTapaggMibCompliance':aristaTapaggMibCompliance,'aristaTapaggMibGroups':aristaTapaggMibGroups,_M:aristaTapaggPolicyGroup})