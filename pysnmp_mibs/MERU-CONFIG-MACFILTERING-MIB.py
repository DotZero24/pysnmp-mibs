_G='mwAclAccessDenyTableIndex'
_F='not-accessible'
_E='mwAclAccessAllowTableIndex'
_D='MERU-CONFIG-MACFILTERING-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigMacFiltering=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,6))
_MwAcl_ObjectIdentity=ObjectIdentity
mwAcl=_MwAcl_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,6,1))
_MwAclCachingTimeout_Type=Unsigned32
_MwAclCachingTimeout_Object=MibScalar
mwAclCachingTimeout=_MwAclCachingTimeout_Object((1,3,6,1,4,1,15983,1,1,4,6,1,4),_MwAclCachingTimeout_Type())
mwAclCachingTimeout.setMaxAccess('read-write')
if mibBuilder.loadTexts:mwAclCachingTimeout.setStatus(_A)
_MwAclAccessAllowTable_Object=MibTable
mwAclAccessAllowTable=_MwAclAccessAllowTable_Object((1,3,6,1,4,1,15983,1,1,4,6,2))
if mibBuilder.loadTexts:mwAclAccessAllowTable.setStatus(_A)
_MwAclAccessAllowEntry_Object=MibTableRow
mwAclAccessAllowEntry=_MwAclAccessAllowEntry_Object((1,3,6,1,4,1,15983,1,1,4,6,2,1))
mwAclAccessAllowEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mwAclAccessAllowEntry.setStatus(_A)
_MwAclAccessAllowTableIndex_Type=Integer32
_MwAclAccessAllowTableIndex_Object=MibTableColumn
mwAclAccessAllowTableIndex=_MwAclAccessAllowTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,6,2,1,1),_MwAclAccessAllowTableIndex_Type())
mwAclAccessAllowTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mwAclAccessAllowTableIndex.setStatus(_A)
_MwAclAccessAllowMac_Type=MacAddress
_MwAclAccessAllowMac_Object=MibTableColumn
mwAclAccessAllowMac=_MwAclAccessAllowMac_Object((1,3,6,1,4,1,15983,1,1,4,6,2,1,2),_MwAclAccessAllowMac_Type())
mwAclAccessAllowMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessAllowMac.setStatus(_A)
class _MwAclAccessAllowDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_MwAclAccessAllowDescr_Type.__name__=_C
_MwAclAccessAllowDescr_Object=MibTableColumn
mwAclAccessAllowDescr=_MwAclAccessAllowDescr_Object((1,3,6,1,4,1,15983,1,1,4,6,2,1,3),_MwAclAccessAllowDescr_Type())
mwAclAccessAllowDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessAllowDescr.setStatus(_A)
_MwAclAccessAllowRowStatus_Type=RowStatus
_MwAclAccessAllowRowStatus_Object=MibTableColumn
mwAclAccessAllowRowStatus=_MwAclAccessAllowRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,6,2,1,5),_MwAclAccessAllowRowStatus_Type())
mwAclAccessAllowRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessAllowRowStatus.setStatus(_A)
_MwAclAccessDenyTable_Object=MibTable
mwAclAccessDenyTable=_MwAclAccessDenyTable_Object((1,3,6,1,4,1,15983,1,1,4,6,3))
if mibBuilder.loadTexts:mwAclAccessDenyTable.setStatus(_A)
_MwAclAccessDenyEntry_Object=MibTableRow
mwAclAccessDenyEntry=_MwAclAccessDenyEntry_Object((1,3,6,1,4,1,15983,1,1,4,6,3,1))
mwAclAccessDenyEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mwAclAccessDenyEntry.setStatus(_A)
_MwAclAccessDenyTableIndex_Type=Integer32
_MwAclAccessDenyTableIndex_Object=MibTableColumn
mwAclAccessDenyTableIndex=_MwAclAccessDenyTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,6,3,1,1),_MwAclAccessDenyTableIndex_Type())
mwAclAccessDenyTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mwAclAccessDenyTableIndex.setStatus(_A)
_MwAclAccessDenyMac_Type=MacAddress
_MwAclAccessDenyMac_Object=MibTableColumn
mwAclAccessDenyMac=_MwAclAccessDenyMac_Object((1,3,6,1,4,1,15983,1,1,4,6,3,1,2),_MwAclAccessDenyMac_Type())
mwAclAccessDenyMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessDenyMac.setStatus(_A)
class _MwAclAccessDenyDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_MwAclAccessDenyDescr_Type.__name__=_C
_MwAclAccessDenyDescr_Object=MibTableColumn
mwAclAccessDenyDescr=_MwAclAccessDenyDescr_Object((1,3,6,1,4,1,15983,1,1,4,6,3,1,3),_MwAclAccessDenyDescr_Type())
mwAclAccessDenyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessDenyDescr.setStatus(_A)
_MwAclAccessDenyRowStatus_Type=RowStatus
_MwAclAccessDenyRowStatus_Object=MibTableColumn
mwAclAccessDenyRowStatus=_MwAclAccessDenyRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,6,3,1,5),_MwAclAccessDenyRowStatus_Type())
mwAclAccessDenyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwAclAccessDenyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigMacFiltering':mwConfigMacFiltering,'mwAcl':mwAcl,'mwAclCachingTimeout':mwAclCachingTimeout,'mwAclAccessAllowTable':mwAclAccessAllowTable,'mwAclAccessAllowEntry':mwAclAccessAllowEntry,_E:mwAclAccessAllowTableIndex,'mwAclAccessAllowMac':mwAclAccessAllowMac,'mwAclAccessAllowDescr':mwAclAccessAllowDescr,'mwAclAccessAllowRowStatus':mwAclAccessAllowRowStatus,'mwAclAccessDenyTable':mwAclAccessDenyTable,'mwAclAccessDenyEntry':mwAclAccessDenyEntry,_G:mwAclAccessDenyTableIndex,'mwAclAccessDenyMac':mwAclAccessDenyMac,'mwAclAccessDenyDescr':mwAclAccessDenyDescr,'mwAclAccessDenyRowStatus':mwAclAccessDenyRowStatus})