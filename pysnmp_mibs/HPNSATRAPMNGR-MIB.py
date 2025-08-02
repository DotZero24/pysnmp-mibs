_O='hpnsaTrapMgrHistTrapHandleIndex'
_N='Critical'
_M='Warning'
_L='Normal'
_K='Informational'
_J='Unknown'
_I='hpnsaTrapMgrActiveTrapHandleIndex'
_H='read-write'
_G='hpnsaTrapMgrAgentIndex'
_F='OctetString'
_E='HPNSATRAPMNGR-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaTrapMgr_ObjectIdentity=ObjectIdentity
hpnsaTrapMgr=_HpnsaTrapMgr_ObjectIdentity((1,3,6,1,4,1,11,2,23,23))
_HpnsaTrapMgrRev_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrRev=_HpnsaTrapMgrRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,1))
class _HpnsaTrapMgrMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaTrapMgrMibRevMajor_Type.__name__=_C
_HpnsaTrapMgrMibRevMajor_Object=MibScalar
hpnsaTrapMgrMibRevMajor=_HpnsaTrapMgrMibRevMajor_Object((1,3,6,1,4,1,11,2,23,23,1,1),_HpnsaTrapMgrMibRevMajor_Type())
hpnsaTrapMgrMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrMibRevMajor.setStatus(_A)
class _HpnsaTrapMgrMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaTrapMgrMibRevMinor_Type.__name__=_C
_HpnsaTrapMgrMibRevMinor_Object=MibScalar
hpnsaTrapMgrMibRevMinor=_HpnsaTrapMgrMibRevMinor_Object((1,3,6,1,4,1,11,2,23,23,1,2),_HpnsaTrapMgrMibRevMinor_Type())
hpnsaTrapMgrMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrMibRevMinor.setStatus(_A)
_HpnsaTrapMgrAgentInfo_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrAgentInfo=_HpnsaTrapMgrAgentInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,2))
_HpnsaTrapMgrAgentTable_Object=MibTable
hpnsaTrapMgrAgentTable=_HpnsaTrapMgrAgentTable_Object((1,3,6,1,4,1,11,2,23,23,2,1))
if mibBuilder.loadTexts:hpnsaTrapMgrAgentTable.setStatus(_A)
_HpnsaTrapMgrAgentEntry_Object=MibTableRow
hpnsaTrapMgrAgentEntry=_HpnsaTrapMgrAgentEntry_Object((1,3,6,1,4,1,11,2,23,23,2,1,1))
hpnsaTrapMgrAgentEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hpnsaTrapMgrAgentEntry.setStatus(_A)
class _HpnsaTrapMgrAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaTrapMgrAgentIndex_Type.__name__=_C
_HpnsaTrapMgrAgentIndex_Object=MibTableColumn
hpnsaTrapMgrAgentIndex=_HpnsaTrapMgrAgentIndex_Object((1,3,6,1,4,1,11,2,23,23,2,1,1,1),_HpnsaTrapMgrAgentIndex_Type())
hpnsaTrapMgrAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrAgentIndex.setStatus(_A)
class _HpnsaTrapMgrAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaTrapMgrAgentName_Type.__name__=_D
_HpnsaTrapMgrAgentName_Object=MibTableColumn
hpnsaTrapMgrAgentName=_HpnsaTrapMgrAgentName_Object((1,3,6,1,4,1,11,2,23,23,2,1,1,2),_HpnsaTrapMgrAgentName_Type())
hpnsaTrapMgrAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrAgentName.setStatus(_A)
class _HpnsaTrapMgrAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaTrapMgrAgentVersion_Type.__name__=_D
_HpnsaTrapMgrAgentVersion_Object=MibTableColumn
hpnsaTrapMgrAgentVersion=_HpnsaTrapMgrAgentVersion_Object((1,3,6,1,4,1,11,2,23,23,2,1,1,3),_HpnsaTrapMgrAgentVersion_Type())
hpnsaTrapMgrAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrAgentVersion.setStatus(_A)
class _HpnsaTrapMgrAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaTrapMgrAgentDate_Type.__name__=_F
_HpnsaTrapMgrAgentDate_Object=MibTableColumn
hpnsaTrapMgrAgentDate=_HpnsaTrapMgrAgentDate_Object((1,3,6,1,4,1,11,2,23,23,2,1,1,4),_HpnsaTrapMgrAgentDate_Type())
hpnsaTrapMgrAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrAgentDate.setStatus(_A)
_HpnsaTrapMgrStats_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrStats=_HpnsaTrapMgrStats_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,3))
class _HpnsaTrapMgrNumActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaTrapMgrNumActive_Type.__name__=_C
_HpnsaTrapMgrNumActive_Object=MibScalar
hpnsaTrapMgrNumActive=_HpnsaTrapMgrNumActive_Object((1,3,6,1,4,1,11,2,23,23,3,1),_HpnsaTrapMgrNumActive_Type())
hpnsaTrapMgrNumActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrNumActive.setStatus(_A)
class _HpnsaTrapMgrNumHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaTrapMgrNumHistory_Type.__name__=_C
_HpnsaTrapMgrNumHistory_Object=MibScalar
hpnsaTrapMgrNumHistory=_HpnsaTrapMgrNumHistory_Object((1,3,6,1,4,1,11,2,23,23,3,2),_HpnsaTrapMgrNumHistory_Type())
hpnsaTrapMgrNumHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrNumHistory.setStatus(_A)
class _HpnsaTrapMgrMaxHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaTrapMgrMaxHistory_Type.__name__=_C
_HpnsaTrapMgrMaxHistory_Object=MibScalar
hpnsaTrapMgrMaxHistory=_HpnsaTrapMgrMaxHistory_Object((1,3,6,1,4,1,11,2,23,23,3,3),_HpnsaTrapMgrMaxHistory_Type())
hpnsaTrapMgrMaxHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrMaxHistory.setStatus(_A)
class _HpnsaTrapMgrEraseTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1234));namedValues=NamedValues(('eraseLogNow',1234))
_HpnsaTrapMgrEraseTraps_Type.__name__=_C
_HpnsaTrapMgrEraseTraps_Object=MibScalar
hpnsaTrapMgrEraseTraps=_HpnsaTrapMgrEraseTraps_Object((1,3,6,1,4,1,11,2,23,23,3,4),_HpnsaTrapMgrEraseTraps_Type())
hpnsaTrapMgrEraseTraps.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaTrapMgrEraseTraps.setStatus(_A)
_HpnsaTrapMgrActive_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrActive=_HpnsaTrapMgrActive_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,4))
_HpnsaTrapMgrActiveTable_Object=MibTable
hpnsaTrapMgrActiveTable=_HpnsaTrapMgrActiveTable_Object((1,3,6,1,4,1,11,2,23,23,4,1))
if mibBuilder.loadTexts:hpnsaTrapMgrActiveTable.setStatus(_A)
_HpnsaTrapMgrActiveTableEntry_Object=MibTableRow
hpnsaTrapMgrActiveTableEntry=_HpnsaTrapMgrActiveTableEntry_Object((1,3,6,1,4,1,11,2,23,23,4,1,1))
hpnsaTrapMgrActiveTableEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnsaTrapMgrActiveTableEntry.setStatus(_A)
class _HpnsaTrapMgrActiveTrapHandleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnsaTrapMgrActiveTrapHandleIndex_Type.__name__=_C
_HpnsaTrapMgrActiveTrapHandleIndex_Object=MibTableColumn
hpnsaTrapMgrActiveTrapHandleIndex=_HpnsaTrapMgrActiveTrapHandleIndex_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,1),_HpnsaTrapMgrActiveTrapHandleIndex_Type())
hpnsaTrapMgrActiveTrapHandleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveTrapHandleIndex.setStatus(_A)
class _HpnsaTrapMgrActiveTrapID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaTrapMgrActiveTrapID_Type.__name__=_D
_HpnsaTrapMgrActiveTrapID_Object=MibTableColumn
hpnsaTrapMgrActiveTrapID=_HpnsaTrapMgrActiveTrapID_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,2),_HpnsaTrapMgrActiveTrapID_Type())
hpnsaTrapMgrActiveTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveTrapID.setStatus(_A)
_HpnsaTrapMgrActiveTimeStamp_Type=Integer32
_HpnsaTrapMgrActiveTimeStamp_Object=MibTableColumn
hpnsaTrapMgrActiveTimeStamp=_HpnsaTrapMgrActiveTimeStamp_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,3),_HpnsaTrapMgrActiveTimeStamp_Type())
hpnsaTrapMgrActiveTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveTimeStamp.setStatus(_A)
class _HpnsaTrapMgrActiveSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_HpnsaTrapMgrActiveSeverity_Type.__name__=_C
_HpnsaTrapMgrActiveSeverity_Object=MibTableColumn
hpnsaTrapMgrActiveSeverity=_HpnsaTrapMgrActiveSeverity_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,4),_HpnsaTrapMgrActiveSeverity_Type())
hpnsaTrapMgrActiveSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveSeverity.setStatus(_A)
class _HpnsaTrapMgrActiveCustomString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnsaTrapMgrActiveCustomString_Type.__name__=_D
_HpnsaTrapMgrActiveCustomString_Object=MibTableColumn
hpnsaTrapMgrActiveCustomString=_HpnsaTrapMgrActiveCustomString_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,5),_HpnsaTrapMgrActiveCustomString_Type())
hpnsaTrapMgrActiveCustomString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveCustomString.setStatus(_A)
class _HpnsaTrapMgrActiveEnterpriseID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaTrapMgrActiveEnterpriseID_Type.__name__=_D
_HpnsaTrapMgrActiveEnterpriseID_Object=MibTableColumn
hpnsaTrapMgrActiveEnterpriseID=_HpnsaTrapMgrActiveEnterpriseID_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,6),_HpnsaTrapMgrActiveEnterpriseID_Type())
hpnsaTrapMgrActiveEnterpriseID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveEnterpriseID.setStatus(_A)
class _HpnsaTrapMgrActiveSpecificID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaTrapMgrActiveSpecificID_Type.__name__=_C
_HpnsaTrapMgrActiveSpecificID_Object=MibTableColumn
hpnsaTrapMgrActiveSpecificID=_HpnsaTrapMgrActiveSpecificID_Object((1,3,6,1,4,1,11,2,23,23,4,1,1,7),_HpnsaTrapMgrActiveSpecificID_Type())
hpnsaTrapMgrActiveSpecificID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrActiveSpecificID.setStatus(_A)
_HpnsaTrapMgrAck_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrAck=_HpnsaTrapMgrAck_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,5))
class _HpnsaTrapMgrTrapHandleAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnsaTrapMgrTrapHandleAck_Type.__name__=_C
_HpnsaTrapMgrTrapHandleAck_Object=MibScalar
hpnsaTrapMgrTrapHandleAck=_HpnsaTrapMgrTrapHandleAck_Object((1,3,6,1,4,1,11,2,23,23,5,1),_HpnsaTrapMgrTrapHandleAck_Type())
hpnsaTrapMgrTrapHandleAck.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaTrapMgrTrapHandleAck.setStatus(_A)
_HpnsaTrapMgrHist_ObjectIdentity=ObjectIdentity
hpnsaTrapMgrHist=_HpnsaTrapMgrHist_ObjectIdentity((1,3,6,1,4,1,11,2,23,23,6))
_HpnsaTrapMgrHistTable_Object=MibTable
hpnsaTrapMgrHistTable=_HpnsaTrapMgrHistTable_Object((1,3,6,1,4,1,11,2,23,23,6,1))
if mibBuilder.loadTexts:hpnsaTrapMgrHistTable.setStatus(_A)
_HpnsaTrapMgrHistTableEntry_Object=MibTableRow
hpnsaTrapMgrHistTableEntry=_HpnsaTrapMgrHistTableEntry_Object((1,3,6,1,4,1,11,2,23,23,6,1,1))
hpnsaTrapMgrHistTableEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hpnsaTrapMgrHistTableEntry.setStatus(_A)
class _HpnsaTrapMgrHistTrapHandleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnsaTrapMgrHistTrapHandleIndex_Type.__name__=_C
_HpnsaTrapMgrHistTrapHandleIndex_Object=MibTableColumn
hpnsaTrapMgrHistTrapHandleIndex=_HpnsaTrapMgrHistTrapHandleIndex_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,1),_HpnsaTrapMgrHistTrapHandleIndex_Type())
hpnsaTrapMgrHistTrapHandleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistTrapHandleIndex.setStatus(_A)
class _HpnsaTrapMgrHistTrapID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaTrapMgrHistTrapID_Type.__name__=_D
_HpnsaTrapMgrHistTrapID_Object=MibTableColumn
hpnsaTrapMgrHistTrapID=_HpnsaTrapMgrHistTrapID_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,2),_HpnsaTrapMgrHistTrapID_Type())
hpnsaTrapMgrHistTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistTrapID.setStatus(_A)
_HpnsaTrapMgrHistTimeStamp_Type=Integer32
_HpnsaTrapMgrHistTimeStamp_Object=MibTableColumn
hpnsaTrapMgrHistTimeStamp=_HpnsaTrapMgrHistTimeStamp_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,3),_HpnsaTrapMgrHistTimeStamp_Type())
hpnsaTrapMgrHistTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistTimeStamp.setStatus(_A)
class _HpnsaTrapMgrHistSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_HpnsaTrapMgrHistSeverity_Type.__name__=_C
_HpnsaTrapMgrHistSeverity_Object=MibTableColumn
hpnsaTrapMgrHistSeverity=_HpnsaTrapMgrHistSeverity_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,4),_HpnsaTrapMgrHistSeverity_Type())
hpnsaTrapMgrHistSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistSeverity.setStatus(_A)
class _HpnsaTrapMgrHistCustomString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnsaTrapMgrHistCustomString_Type.__name__=_D
_HpnsaTrapMgrHistCustomString_Object=MibTableColumn
hpnsaTrapMgrHistCustomString=_HpnsaTrapMgrHistCustomString_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,5),_HpnsaTrapMgrHistCustomString_Type())
hpnsaTrapMgrHistCustomString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistCustomString.setStatus(_A)
class _HpnsaTrapMgrHistEnterpriseID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnsaTrapMgrHistEnterpriseID_Type.__name__=_D
_HpnsaTrapMgrHistEnterpriseID_Object=MibTableColumn
hpnsaTrapMgrHistEnterpriseID=_HpnsaTrapMgrHistEnterpriseID_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,6),_HpnsaTrapMgrHistEnterpriseID_Type())
hpnsaTrapMgrHistEnterpriseID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistEnterpriseID.setStatus(_A)
class _HpnsaTrapMgrHistSpecificID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaTrapMgrHistSpecificID_Type.__name__=_C
_HpnsaTrapMgrHistSpecificID_Object=MibTableColumn
hpnsaTrapMgrHistSpecificID=_HpnsaTrapMgrHistSpecificID_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,7),_HpnsaTrapMgrHistSpecificID_Type())
hpnsaTrapMgrHistSpecificID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistSpecificID.setStatus(_A)
class _HpnsaTrapMgrHistAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ACTIVE',0),('ACKNOWLEDGED',1)))
_HpnsaTrapMgrHistAck_Type.__name__=_C
_HpnsaTrapMgrHistAck_Object=MibTableColumn
hpnsaTrapMgrHistAck=_HpnsaTrapMgrHistAck_Object((1,3,6,1,4,1,11,2,23,23,6,1,1,8),_HpnsaTrapMgrHistAck_Type())
hpnsaTrapMgrHistAck.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTrapMgrHistAck.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaTrapMgr':hpnsaTrapMgr,'hpnsaTrapMgrRev':hpnsaTrapMgrRev,'hpnsaTrapMgrMibRevMajor':hpnsaTrapMgrMibRevMajor,'hpnsaTrapMgrMibRevMinor':hpnsaTrapMgrMibRevMinor,'hpnsaTrapMgrAgentInfo':hpnsaTrapMgrAgentInfo,'hpnsaTrapMgrAgentTable':hpnsaTrapMgrAgentTable,'hpnsaTrapMgrAgentEntry':hpnsaTrapMgrAgentEntry,_G:hpnsaTrapMgrAgentIndex,'hpnsaTrapMgrAgentName':hpnsaTrapMgrAgentName,'hpnsaTrapMgrAgentVersion':hpnsaTrapMgrAgentVersion,'hpnsaTrapMgrAgentDate':hpnsaTrapMgrAgentDate,'hpnsaTrapMgrStats':hpnsaTrapMgrStats,'hpnsaTrapMgrNumActive':hpnsaTrapMgrNumActive,'hpnsaTrapMgrNumHistory':hpnsaTrapMgrNumHistory,'hpnsaTrapMgrMaxHistory':hpnsaTrapMgrMaxHistory,'hpnsaTrapMgrEraseTraps':hpnsaTrapMgrEraseTraps,'hpnsaTrapMgrActive':hpnsaTrapMgrActive,'hpnsaTrapMgrActiveTable':hpnsaTrapMgrActiveTable,'hpnsaTrapMgrActiveTableEntry':hpnsaTrapMgrActiveTableEntry,_I:hpnsaTrapMgrActiveTrapHandleIndex,'hpnsaTrapMgrActiveTrapID':hpnsaTrapMgrActiveTrapID,'hpnsaTrapMgrActiveTimeStamp':hpnsaTrapMgrActiveTimeStamp,'hpnsaTrapMgrActiveSeverity':hpnsaTrapMgrActiveSeverity,'hpnsaTrapMgrActiveCustomString':hpnsaTrapMgrActiveCustomString,'hpnsaTrapMgrActiveEnterpriseID':hpnsaTrapMgrActiveEnterpriseID,'hpnsaTrapMgrActiveSpecificID':hpnsaTrapMgrActiveSpecificID,'hpnsaTrapMgrAck':hpnsaTrapMgrAck,'hpnsaTrapMgrTrapHandleAck':hpnsaTrapMgrTrapHandleAck,'hpnsaTrapMgrHist':hpnsaTrapMgrHist,'hpnsaTrapMgrHistTable':hpnsaTrapMgrHistTable,'hpnsaTrapMgrHistTableEntry':hpnsaTrapMgrHistTableEntry,_O:hpnsaTrapMgrHistTrapHandleIndex,'hpnsaTrapMgrHistTrapID':hpnsaTrapMgrHistTrapID,'hpnsaTrapMgrHistTimeStamp':hpnsaTrapMgrHistTimeStamp,'hpnsaTrapMgrHistSeverity':hpnsaTrapMgrHistSeverity,'hpnsaTrapMgrHistCustomString':hpnsaTrapMgrHistCustomString,'hpnsaTrapMgrHistEnterpriseID':hpnsaTrapMgrHistEnterpriseID,'hpnsaTrapMgrHistSpecificID':hpnsaTrapMgrHistSpecificID,'hpnsaTrapMgrHistAck':hpnsaTrapMgrHistAck})