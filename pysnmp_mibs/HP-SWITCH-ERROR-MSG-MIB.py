_N='hpSwitchErrorMsgMIBGroup'
_M='hpSwitchSnmpErrorCode'
_L='hpSwitchEntityErrorMsg'
_K='hpSwitchErrorFailedOID'
_J='hpSwitchErrorTime'
_I='hpSwitchErrorSnmpSeqCode'
_H='hpSwitchErrorEntityHandle'
_G='hpSwitchErrorEntityType'
_F='OctetString'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='HP-SWITCH-ERROR-MSG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
hpSwitchErrorMsgMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,68))
if mibBuilder.loadTexts:hpSwitchErrorMsgMIB.setRevisions(('2009-04-06 00:00',))
_HpSwitchErrorMsgObjects_ObjectIdentity=ObjectIdentity
hpSwitchErrorMsgObjects=_HpSwitchErrorMsgObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,68,1))
_HpSwitchErrorMsgTable_Object=MibTable
hpSwitchErrorMsgTable=_HpSwitchErrorMsgTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1))
if mibBuilder.loadTexts:hpSwitchErrorMsgTable.setStatus(_A)
_HpSwitchErrorMsgEntry_Object=MibTableRow
hpSwitchErrorMsgEntry=_HpSwitchErrorMsgEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1))
hpSwitchErrorMsgEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpSwitchErrorMsgEntry.setStatus(_A)
class _HpSwitchErrorEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('others',1),('cliSession',2),('webSession',3),('ipV4Address',4),('ipV6Address',5),('oaApplication',6)))
_HpSwitchErrorEntityType_Type.__name__=_C
_HpSwitchErrorEntityType_Object=MibTableColumn
hpSwitchErrorEntityType=_HpSwitchErrorEntityType_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,1),_HpSwitchErrorEntityType_Type())
hpSwitchErrorEntityType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchErrorEntityType.setStatus(_A)
class _HpSwitchErrorEntityHandle_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_HpSwitchErrorEntityHandle_Type.__name__=_F
_HpSwitchErrorEntityHandle_Object=MibTableColumn
hpSwitchErrorEntityHandle=_HpSwitchErrorEntityHandle_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,2),_HpSwitchErrorEntityHandle_Type())
hpSwitchErrorEntityHandle.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchErrorEntityHandle.setStatus(_A)
class _HpSwitchErrorSnmpSeqCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpSwitchErrorSnmpSeqCode_Type.__name__=_C
_HpSwitchErrorSnmpSeqCode_Object=MibTableColumn
hpSwitchErrorSnmpSeqCode=_HpSwitchErrorSnmpSeqCode_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,3),_HpSwitchErrorSnmpSeqCode_Type())
hpSwitchErrorSnmpSeqCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchErrorSnmpSeqCode.setStatus(_A)
_HpSwitchErrorTime_Type=DateAndTime
_HpSwitchErrorTime_Object=MibTableColumn
hpSwitchErrorTime=_HpSwitchErrorTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,4),_HpSwitchErrorTime_Type())
hpSwitchErrorTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchErrorTime.setStatus(_A)
_HpSwitchErrorFailedOID_Type=ObjectIdentifier
_HpSwitchErrorFailedOID_Object=MibTableColumn
hpSwitchErrorFailedOID=_HpSwitchErrorFailedOID_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,5),_HpSwitchErrorFailedOID_Type())
hpSwitchErrorFailedOID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchErrorFailedOID.setStatus(_A)
_HpSwitchEntityErrorMsg_Type=OctetString
_HpSwitchEntityErrorMsg_Object=MibTableColumn
hpSwitchEntityErrorMsg=_HpSwitchEntityErrorMsg_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,6),_HpSwitchEntityErrorMsg_Type())
hpSwitchEntityErrorMsg.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchEntityErrorMsg.setStatus(_A)
class _HpSwitchSnmpErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18))
_HpSwitchSnmpErrorCode_Type.__name__=_C
_HpSwitchSnmpErrorCode_Object=MibTableColumn
hpSwitchSnmpErrorCode=_HpSwitchSnmpErrorCode_Object((1,3,6,1,4,1,11,2,14,11,5,1,68,1,1,1,7),_HpSwitchSnmpErrorCode_Type())
hpSwitchSnmpErrorCode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSnmpErrorCode.setStatus(_A)
_HpSwitchErrorMsgMIBConformance_ObjectIdentity=ObjectIdentity
hpSwitchErrorMsgMIBConformance=_HpSwitchErrorMsgMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,68,2))
_HpSwitchErrorMsgMIBCompliances_ObjectIdentity=ObjectIdentity
hpSwitchErrorMsgMIBCompliances=_HpSwitchErrorMsgMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,68,2,1))
_HpSwitchErrorMsgMIBGroups_ObjectIdentity=ObjectIdentity
hpSwitchErrorMsgMIBGroups=_HpSwitchErrorMsgMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,68,2,2))
hpSwitchErrorMsgMIBGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,68,2,2,1))
hpSwitchErrorMsgMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpSwitchErrorMsgMIBGroup.setStatus(_A)
hpSwitchErrorMsgMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,68,2,1,1))
hpSwitchErrorMsgMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:hpSwitchErrorMsgMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpSwitchErrorMsgMIB':hpSwitchErrorMsgMIB,'hpSwitchErrorMsgObjects':hpSwitchErrorMsgObjects,'hpSwitchErrorMsgTable':hpSwitchErrorMsgTable,'hpSwitchErrorMsgEntry':hpSwitchErrorMsgEntry,_G:hpSwitchErrorEntityType,_H:hpSwitchErrorEntityHandle,_I:hpSwitchErrorSnmpSeqCode,_J:hpSwitchErrorTime,_K:hpSwitchErrorFailedOID,_L:hpSwitchEntityErrorMsg,_M:hpSwitchSnmpErrorCode,'hpSwitchErrorMsgMIBConformance':hpSwitchErrorMsgMIBConformance,'hpSwitchErrorMsgMIBCompliances':hpSwitchErrorMsgMIBCompliances,'hpSwitchErrorMsgMIBCompliance':hpSwitchErrorMsgMIBCompliance,'hpSwitchErrorMsgMIBGroups':hpSwitchErrorMsgMIBGroups,_N:hpSwitchErrorMsgMIBGroup})