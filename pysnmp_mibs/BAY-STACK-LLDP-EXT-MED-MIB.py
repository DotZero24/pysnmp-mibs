_G='bsLldpXMedLocMediaPolicyAppType'
_F='BAY-STACK-LLDP-EXT-MED-MIB'
_E='Integer32'
_D='lldpLocPortNum'
_C='LLDP-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
PolicyAppType,=mibBuilder.importSymbols('LLDP-EXT-MED-MIB','PolicyAppType')
lldpLocPortNum,=mibBuilder.importSymbols(_C,_D)
VlanIdOrAnyOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrAnyOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackLldpExtMedMib=ModuleIdentity((1,3,6,1,4,1,45,5,33))
if mibBuilder.loadTexts:bayStackLldpExtMedMib.setRevisions(('2009-03-30 00:00',))
_BsLldpExtMedNotifications_ObjectIdentity=ObjectIdentity
bsLldpExtMedNotifications=_BsLldpExtMedNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,33,0))
_BsLldpExtMedObjects_ObjectIdentity=ObjectIdentity
bsLldpExtMedObjects=_BsLldpExtMedObjects_ObjectIdentity((1,3,6,1,4,1,45,5,33,1))
_BsLldpXMedLocMediaPolicyTable_Object=MibTable
bsLldpXMedLocMediaPolicyTable=_BsLldpXMedLocMediaPolicyTable_Object((1,3,6,1,4,1,45,5,33,1,1))
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyTable.setStatus(_A)
_BsLldpXMedLocMediaPolicyEntry_Object=MibTableRow
bsLldpXMedLocMediaPolicyEntry=_BsLldpXMedLocMediaPolicyEntry_Object((1,3,6,1,4,1,45,5,33,1,1,1))
bsLldpXMedLocMediaPolicyEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyEntry.setStatus(_A)
_BsLldpXMedLocMediaPolicyAppType_Type=PolicyAppType
_BsLldpXMedLocMediaPolicyAppType_Object=MibTableColumn
bsLldpXMedLocMediaPolicyAppType=_BsLldpXMedLocMediaPolicyAppType_Object((1,3,6,1,4,1,45,5,33,1,1,1,1),_BsLldpXMedLocMediaPolicyAppType_Type())
bsLldpXMedLocMediaPolicyAppType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyAppType.setStatus(_A)
_BsLldpXMedLocMediaPolicyVlanID_Type=VlanIdOrAnyOrNone
_BsLldpXMedLocMediaPolicyVlanID_Object=MibTableColumn
bsLldpXMedLocMediaPolicyVlanID=_BsLldpXMedLocMediaPolicyVlanID_Object((1,3,6,1,4,1,45,5,33,1,1,1,2),_BsLldpXMedLocMediaPolicyVlanID_Type())
bsLldpXMedLocMediaPolicyVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyVlanID.setStatus(_A)
class _BsLldpXMedLocMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BsLldpXMedLocMediaPolicyPriority_Type.__name__=_E
_BsLldpXMedLocMediaPolicyPriority_Object=MibTableColumn
bsLldpXMedLocMediaPolicyPriority=_BsLldpXMedLocMediaPolicyPriority_Object((1,3,6,1,4,1,45,5,33,1,1,1,3),_BsLldpXMedLocMediaPolicyPriority_Type())
bsLldpXMedLocMediaPolicyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyPriority.setStatus(_A)
_BsLldpXMedLocMediaPolicyDscp_Type=Dscp
_BsLldpXMedLocMediaPolicyDscp_Object=MibTableColumn
bsLldpXMedLocMediaPolicyDscp=_BsLldpXMedLocMediaPolicyDscp_Object((1,3,6,1,4,1,45,5,33,1,1,1,4),_BsLldpXMedLocMediaPolicyDscp_Type())
bsLldpXMedLocMediaPolicyDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyDscp.setStatus(_A)
_BsLldpXMedLocMediaPolicyUnknown_Type=TruthValue
_BsLldpXMedLocMediaPolicyUnknown_Object=MibTableColumn
bsLldpXMedLocMediaPolicyUnknown=_BsLldpXMedLocMediaPolicyUnknown_Object((1,3,6,1,4,1,45,5,33,1,1,1,5),_BsLldpXMedLocMediaPolicyUnknown_Type())
bsLldpXMedLocMediaPolicyUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyUnknown.setStatus(_A)
_BsLldpXMedLocMediaPolicyTagged_Type=TruthValue
_BsLldpXMedLocMediaPolicyTagged_Object=MibTableColumn
bsLldpXMedLocMediaPolicyTagged=_BsLldpXMedLocMediaPolicyTagged_Object((1,3,6,1,4,1,45,5,33,1,1,1,6),_BsLldpXMedLocMediaPolicyTagged_Type())
bsLldpXMedLocMediaPolicyTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyTagged.setStatus(_A)
_BsLldpXMedLocMediaPolicyRowStatus_Type=RowStatus
_BsLldpXMedLocMediaPolicyRowStatus_Object=MibTableColumn
bsLldpXMedLocMediaPolicyRowStatus=_BsLldpXMedLocMediaPolicyRowStatus_Object((1,3,6,1,4,1,45,5,33,1,1,1,7),_BsLldpXMedLocMediaPolicyRowStatus_Type())
bsLldpXMedLocMediaPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsLldpXMedLocMediaPolicyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'bayStackLldpExtMedMib':bayStackLldpExtMedMib,'bsLldpExtMedNotifications':bsLldpExtMedNotifications,'bsLldpExtMedObjects':bsLldpExtMedObjects,'bsLldpXMedLocMediaPolicyTable':bsLldpXMedLocMediaPolicyTable,'bsLldpXMedLocMediaPolicyEntry':bsLldpXMedLocMediaPolicyEntry,_G:bsLldpXMedLocMediaPolicyAppType,'bsLldpXMedLocMediaPolicyVlanID':bsLldpXMedLocMediaPolicyVlanID,'bsLldpXMedLocMediaPolicyPriority':bsLldpXMedLocMediaPolicyPriority,'bsLldpXMedLocMediaPolicyDscp':bsLldpXMedLocMediaPolicyDscp,'bsLldpXMedLocMediaPolicyUnknown':bsLldpXMedLocMediaPolicyUnknown,'bsLldpXMedLocMediaPolicyTagged':bsLldpXMedLocMediaPolicyTagged,'bsLldpXMedLocMediaPolicyRowStatus':bsLldpXMedLocMediaPolicyRowStatus})