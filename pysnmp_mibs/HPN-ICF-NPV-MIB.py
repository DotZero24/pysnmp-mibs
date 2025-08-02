_G='read-only'
_F='read-create'
_E='ifIndex'
_D='IF-MIB'
_C='hpnicfVsanIndex'
_B='HPN-ICF-VSAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcVsanIndex,=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcVsanIndex')
hpnicfSan,hpnicfVsanIndex=mibBuilder.importSymbols(_B,'hpnicfSan',_C)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
hpnicfNpv=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,6))
if mibBuilder.loadTexts:hpnicfNpv.setRevisions(('2013-04-02 00:00',))
class HpnicfNpvIfIndexList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,65535))
_HpnicfNpvMibObjects_ObjectIdentity=ObjectIdentity
hpnicfNpvMibObjects=_HpnicfNpvMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1))
_HpnicfNpvConfiguration_ObjectIdentity=ObjectIdentity
hpnicfNpvConfiguration=_HpnicfNpvConfiguration_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1))
_HpnicfNpvGlobalObjects_ObjectIdentity=ObjectIdentity
hpnicfNpvGlobalObjects=_HpnicfNpvGlobalObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,1))
_HpnicfNpvLoadbalanceVsan_Type=HpnicfFcVsanIndex
_HpnicfNpvLoadbalanceVsan_Object=MibScalar
hpnicfNpvLoadbalanceVsan=_HpnicfNpvLoadbalanceVsan_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,1,1),_HpnicfNpvLoadbalanceVsan_Type())
hpnicfNpvLoadbalanceVsan.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfNpvLoadbalanceVsan.setStatus(_A)
_HpnicfNpvTrafficMapConfigTable_Object=MibTable
hpnicfNpvTrafficMapConfigTable=_HpnicfNpvTrafficMapConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,2))
if mibBuilder.loadTexts:hpnicfNpvTrafficMapConfigTable.setStatus(_A)
_HpnicfNpvTrafficMapConfigEntry_Object=MibTableRow
hpnicfNpvTrafficMapConfigEntry=_HpnicfNpvTrafficMapConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,2,1))
hpnicfNpvTrafficMapConfigEntry.setIndexNames((0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:hpnicfNpvTrafficMapConfigEntry.setStatus(_A)
_HpnicfNpvTrafficMapExternalIfIndexList_Type=HpnicfNpvIfIndexList
_HpnicfNpvTrafficMapExternalIfIndexList_Object=MibTableColumn
hpnicfNpvTrafficMapExternalIfIndexList=_HpnicfNpvTrafficMapExternalIfIndexList_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,2,1,1),_HpnicfNpvTrafficMapExternalIfIndexList_Type())
hpnicfNpvTrafficMapExternalIfIndexList.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNpvTrafficMapExternalIfIndexList.setStatus(_A)
_HpnicfNpvTrafficMapLastChange_Type=TimeStamp
_HpnicfNpvTrafficMapLastChange_Object=MibTableColumn
hpnicfNpvTrafficMapLastChange=_HpnicfNpvTrafficMapLastChange_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,2,1,2),_HpnicfNpvTrafficMapLastChange_Type())
hpnicfNpvTrafficMapLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNpvTrafficMapLastChange.setStatus(_A)
_HpnicfNpvTrafficMapRowStatus_Type=RowStatus
_HpnicfNpvTrafficMapRowStatus_Object=MibTableColumn
hpnicfNpvTrafficMapRowStatus=_HpnicfNpvTrafficMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,2,1,3),_HpnicfNpvTrafficMapRowStatus_Type())
hpnicfNpvTrafficMapRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfNpvTrafficMapRowStatus.setStatus(_A)
_HpnicfNpvServerIfTable_Object=MibTable
hpnicfNpvServerIfTable=_HpnicfNpvServerIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,3))
if mibBuilder.loadTexts:hpnicfNpvServerIfTable.setStatus(_A)
_HpnicfNpvServerIfEntry_Object=MibTableRow
hpnicfNpvServerIfEntry=_HpnicfNpvServerIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,3,1))
hpnicfNpvServerIfEntry.setIndexNames((0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:hpnicfNpvServerIfEntry.setStatus(_A)
_HpnicfNpvExternalIfIndex_Type=InterfaceIndex
_HpnicfNpvExternalIfIndex_Object=MibTableColumn
hpnicfNpvExternalIfIndex=_HpnicfNpvExternalIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,6,1,1,3,1,1),_HpnicfNpvExternalIfIndex_Type())
hpnicfNpvExternalIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfNpvExternalIfIndex.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-NPV-MIB',**{'HpnicfNpvIfIndexList':HpnicfNpvIfIndexList,'hpnicfNpv':hpnicfNpv,'hpnicfNpvMibObjects':hpnicfNpvMibObjects,'hpnicfNpvConfiguration':hpnicfNpvConfiguration,'hpnicfNpvGlobalObjects':hpnicfNpvGlobalObjects,'hpnicfNpvLoadbalanceVsan':hpnicfNpvLoadbalanceVsan,'hpnicfNpvTrafficMapConfigTable':hpnicfNpvTrafficMapConfigTable,'hpnicfNpvTrafficMapConfigEntry':hpnicfNpvTrafficMapConfigEntry,'hpnicfNpvTrafficMapExternalIfIndexList':hpnicfNpvTrafficMapExternalIfIndexList,'hpnicfNpvTrafficMapLastChange':hpnicfNpvTrafficMapLastChange,'hpnicfNpvTrafficMapRowStatus':hpnicfNpvTrafficMapRowStatus,'hpnicfNpvServerIfTable':hpnicfNpvServerIfTable,'hpnicfNpvServerIfEntry':hpnicfNpvServerIfEntry,'hpnicfNpvExternalIfIndex':hpnicfNpvExternalIfIndex})