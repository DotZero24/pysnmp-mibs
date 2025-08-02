_O='sfpsMcastIPSIBSender'
_N='sfpsMcastIPSIBGroup'
_M='undoExclude'
_L='undoInclude'
_K='exclude'
_J='include'
_I='sfpsMcastIPRIBGroup'
_H='sfpsMcastIPRouterIfNum'
_G='other'
_F='deprecated'
_E='CTRON-SFPS-MCAST-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsMcastCnx,sfpsMcastCnxAPI,sfpsMcastConfigApi,sfpsMcastIPRIBApi,sfpsMcastIPReceiverInfoBase,sfpsMcastIPRouter,sfpsMcastIPSIBApi,sfpsMcastIPSenderInfoBase=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsMcastCnx','sfpsMcastCnxAPI','sfpsMcastConfigApi','sfpsMcastIPRIBApi','sfpsMcastIPReceiverInfoBase','sfpsMcastIPRouter','sfpsMcastIPSIBApi','sfpsMcastIPSenderInfoBase')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsMcastCnxDestination_Type=SfpsAddress
_SfpsMcastCnxDestination_Object=MibScalar
sfpsMcastCnxDestination=_SfpsMcastCnxDestination_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,1),_SfpsMcastCnxDestination_Type())
sfpsMcastCnxDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxDestination.setStatus(_A)
_SfpsMcastCnxSource_Type=SfpsAddress
_SfpsMcastCnxSource_Object=MibScalar
sfpsMcastCnxSource=_SfpsMcastCnxSource_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,2),_SfpsMcastCnxSource_Type())
sfpsMcastCnxSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxSource.setStatus(_A)
_SfpsMcastCnxSenderSw_Type=SfpsAddress
_SfpsMcastCnxSenderSw_Object=MibScalar
sfpsMcastCnxSenderSw=_SfpsMcastCnxSenderSw_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,3),_SfpsMcastCnxSenderSw_Type())
sfpsMcastCnxSenderSw.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxSenderSw.setStatus(_A)
_SfpsMcastCnxInPort_Type=Integer32
_SfpsMcastCnxInPort_Object=MibScalar
sfpsMcastCnxInPort=_SfpsMcastCnxInPort_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,4),_SfpsMcastCnxInPort_Type())
sfpsMcastCnxInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxInPort.setStatus(_A)
_SfpsMcastCnxOutPorts_Type=DisplayString
_SfpsMcastCnxOutPorts_Object=MibScalar
sfpsMcastCnxOutPorts=_SfpsMcastCnxOutPorts_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,5),_SfpsMcastCnxOutPorts_Type())
sfpsMcastCnxOutPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxOutPorts.setStatus(_A)
_SfpsMcastCnxGroup_Type=IpAddress
_SfpsMcastCnxGroup_Object=MibScalar
sfpsMcastCnxGroup=_SfpsMcastCnxGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,6),_SfpsMcastCnxGroup_Type())
sfpsMcastCnxGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxGroup.setStatus(_A)
_SfpsMcastCnxTTL_Type=Integer32
_SfpsMcastCnxTTL_Object=MibScalar
sfpsMcastCnxTTL=_SfpsMcastCnxTTL_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,7),_SfpsMcastCnxTTL_Type())
sfpsMcastCnxTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxTTL.setStatus(_F)
_SfpsMcastCnxAge_Type=TimeTicks
_SfpsMcastCnxAge_Object=MibScalar
sfpsMcastCnxAge=_SfpsMcastCnxAge_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,8),_SfpsMcastCnxAge_Type())
sfpsMcastCnxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAge.setStatus(_A)
class _SfpsMcastCnxStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,8,16,17,18)));namedValues=NamedValues(*(('filter',1),('inActive',2),('remote',4),('netFilter',5),('dying',8),('static',16),('staticFilter',17),('staticInactive',18)))
_SfpsMcastCnxStatus_Type.__name__=_C
_SfpsMcastCnxStatus_Object=MibScalar
sfpsMcastCnxStatus=_SfpsMcastCnxStatus_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,9),_SfpsMcastCnxStatus_Type())
sfpsMcastCnxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxStatus.setStatus(_A)
_SfpsMcastCnxNextSw_Type=SfpsAddress
_SfpsMcastCnxNextSw_Object=MibScalar
sfpsMcastCnxNextSw=_SfpsMcastCnxNextSw_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,1,10),_SfpsMcastCnxNextSw_Type())
sfpsMcastCnxNextSw.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxNextSw.setStatus(_A)
_SfpsMcastCnxAPIDestination_Type=SfpsAddress
_SfpsMcastCnxAPIDestination_Object=MibScalar
sfpsMcastCnxAPIDestination=_SfpsMcastCnxAPIDestination_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,1),_SfpsMcastCnxAPIDestination_Type())
sfpsMcastCnxAPIDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIDestination.setStatus(_A)
_SfpsMcastCnxAPISource_Type=SfpsAddress
_SfpsMcastCnxAPISource_Object=MibScalar
sfpsMcastCnxAPISource=_SfpsMcastCnxAPISource_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,2),_SfpsMcastCnxAPISource_Type())
sfpsMcastCnxAPISource.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPISource.setStatus(_A)
_SfpsMcastCnxAPISenderSw_Type=SfpsAddress
_SfpsMcastCnxAPISenderSw_Object=MibScalar
sfpsMcastCnxAPISenderSw=_SfpsMcastCnxAPISenderSw_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,3),_SfpsMcastCnxAPISenderSw_Type())
sfpsMcastCnxAPISenderSw.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPISenderSw.setStatus(_A)
_SfpsMcastCnxAPIInPort_Type=Integer32
_SfpsMcastCnxAPIInPort_Object=MibScalar
sfpsMcastCnxAPIInPort=_SfpsMcastCnxAPIInPort_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,4),_SfpsMcastCnxAPIInPort_Type())
sfpsMcastCnxAPIInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIInPort.setStatus(_A)
_SfpsMcastCnxAPIOutPort_Type=DisplayString
_SfpsMcastCnxAPIOutPort_Object=MibScalar
sfpsMcastCnxAPIOutPort=_SfpsMcastCnxAPIOutPort_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,5),_SfpsMcastCnxAPIOutPort_Type())
sfpsMcastCnxAPIOutPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIOutPort.setStatus(_A)
_SfpsMcastCnxAPIGroup_Type=IpAddress
_SfpsMcastCnxAPIGroup_Object=MibScalar
sfpsMcastCnxAPIGroup=_SfpsMcastCnxAPIGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,6),_SfpsMcastCnxAPIGroup_Type())
sfpsMcastCnxAPIGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIGroup.setStatus(_A)
_SfpsMcastCnxAPITTL_Type=Integer32
_SfpsMcastCnxAPITTL_Object=MibScalar
sfpsMcastCnxAPITTL=_SfpsMcastCnxAPITTL_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,7),_SfpsMcastCnxAPITTL_Type())
sfpsMcastCnxAPITTL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPITTL.setStatus(_F)
class _SfpsMcastCnxAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('addFilter',2),('addPort',3),('delPort',4),('addCnx',5),('delCnx',6)))
_SfpsMcastCnxAPIVerb_Type.__name__=_C
_SfpsMcastCnxAPIVerb_Object=MibScalar
sfpsMcastCnxAPIVerb=_SfpsMcastCnxAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,8),_SfpsMcastCnxAPIVerb_Type())
sfpsMcastCnxAPIVerb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIVerb.setStatus(_A)
_SfpsMcastCnxAPIFilters_Type=Integer32
_SfpsMcastCnxAPIFilters_Object=MibScalar
sfpsMcastCnxAPIFilters=_SfpsMcastCnxAPIFilters_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,9),_SfpsMcastCnxAPIFilters_Type())
sfpsMcastCnxAPIFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPIFilters.setStatus(_A)
_SfpsMcastCnxAPINonFilters_Type=Integer32
_SfpsMcastCnxAPINonFilters_Object=MibScalar
sfpsMcastCnxAPINonFilters=_SfpsMcastCnxAPINonFilters_Object((1,3,6,1,4,1,52,4,2,4,2,5,1,2,10),_SfpsMcastCnxAPINonFilters_Type())
sfpsMcastCnxAPINonFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastCnxAPINonFilters.setStatus(_A)
_SfpsMcastIPRouterTable_Object=MibTable
sfpsMcastIPRouterTable=_SfpsMcastIPRouterTable_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1))
if mibBuilder.loadTexts:sfpsMcastIPRouterTable.setStatus(_A)
_SfpsMcastIPRouterEntry_Object=MibTableRow
sfpsMcastIPRouterEntry=_SfpsMcastIPRouterEntry_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1,1))
sfpsMcastIPRouterEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:sfpsMcastIPRouterEntry.setStatus(_A)
_SfpsMcastIPRouterIfNum_Type=Integer32
_SfpsMcastIPRouterIfNum_Object=MibTableColumn
sfpsMcastIPRouterIfNum=_SfpsMcastIPRouterIfNum_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1,1,1),_SfpsMcastIPRouterIfNum_Type())
sfpsMcastIPRouterIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRouterIfNum.setStatus(_A)
_SfpsMcastIPRouterVlanId_Type=Integer32
_SfpsMcastIPRouterVlanId_Object=MibTableColumn
sfpsMcastIPRouterVlanId=_SfpsMcastIPRouterVlanId_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1,1,2),_SfpsMcastIPRouterVlanId_Type())
sfpsMcastIPRouterVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRouterVlanId.setStatus(_A)
_SfpsMcastIPRouterRouterIP_Type=IpAddress
_SfpsMcastIPRouterRouterIP_Object=MibTableColumn
sfpsMcastIPRouterRouterIP=_SfpsMcastIPRouterRouterIP_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1,1,3),_SfpsMcastIPRouterRouterIP_Type())
sfpsMcastIPRouterRouterIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRouterRouterIP.setStatus(_A)
_SfpsMcastIPRouterTTL_Type=Integer32
_SfpsMcastIPRouterTTL_Object=MibTableColumn
sfpsMcastIPRouterTTL=_SfpsMcastIPRouterTTL_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,1,1,4),_SfpsMcastIPRouterTTL_Type())
sfpsMcastIPRouterTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRouterTTL.setStatus(_F)
class _SfpsMcastIPRouterAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('portMap',2),('portUnmap',3)))
_SfpsMcastIPRouterAPIVerb_Type.__name__=_C
_SfpsMcastIPRouterAPIVerb_Object=MibScalar
sfpsMcastIPRouterAPIVerb=_SfpsMcastIPRouterAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,2),_SfpsMcastIPRouterAPIVerb_Type())
sfpsMcastIPRouterAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPRouterAPIVerb.setStatus(_A)
_SfpsMcastIPRouterAPIIFNum_Type=Integer32
_SfpsMcastIPRouterAPIIFNum_Object=MibScalar
sfpsMcastIPRouterAPIIFNum=_SfpsMcastIPRouterAPIIFNum_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,3),_SfpsMcastIPRouterAPIIFNum_Type())
sfpsMcastIPRouterAPIIFNum.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPRouterAPIIFNum.setStatus(_A)
_SfpsMcastIPRouterAPIRouterIP_Type=IpAddress
_SfpsMcastIPRouterAPIRouterIP_Object=MibScalar
sfpsMcastIPRouterAPIRouterIP=_SfpsMcastIPRouterAPIRouterIP_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,4),_SfpsMcastIPRouterAPIRouterIP_Type())
sfpsMcastIPRouterAPIRouterIP.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPRouterAPIRouterIP.setStatus(_A)
class _SfpsMcastIPRouterAPITTLScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,16,64,128,192,255)));namedValues=NamedValues(*(('subnet',1),('vacinity',4),('site',16),('region',64),('world',128),('worldLimited',192),('unrestricted',255)))
_SfpsMcastIPRouterAPITTLScope_Type.__name__=_C
_SfpsMcastIPRouterAPITTLScope_Object=MibScalar
sfpsMcastIPRouterAPITTLScope=_SfpsMcastIPRouterAPITTLScope_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,5),_SfpsMcastIPRouterAPITTLScope_Type())
sfpsMcastIPRouterAPITTLScope.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPRouterAPITTLScope.setStatus(_F)
_SfpsMcastIPRouterAPIVlanId_Type=Integer32
_SfpsMcastIPRouterAPIVlanId_Object=MibScalar
sfpsMcastIPRouterAPIVlanId=_SfpsMcastIPRouterAPIVlanId_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,1,6),_SfpsMcastIPRouterAPIVlanId_Type())
sfpsMcastIPRouterAPIVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPRouterAPIVlanId.setStatus(_A)
_SfpsMcastIPRIBTable_Object=MibTable
sfpsMcastIPRIBTable=_SfpsMcastIPRIBTable_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1))
if mibBuilder.loadTexts:sfpsMcastIPRIBTable.setStatus(_A)
_SfpsMcastIPRIBEntry_Object=MibTableRow
sfpsMcastIPRIBEntry=_SfpsMcastIPRIBEntry_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1))
sfpsMcastIPRIBEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:sfpsMcastIPRIBEntry.setStatus(_A)
_SfpsMcastIPRIBGroup_Type=IpAddress
_SfpsMcastIPRIBGroup_Object=MibTableColumn
sfpsMcastIPRIBGroup=_SfpsMcastIPRIBGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1,1),_SfpsMcastIPRIBGroup_Type())
sfpsMcastIPRIBGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBGroup.setStatus(_A)
class _SfpsMcastIPRIBOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('local',2),('router',3),('igmp',4),('netMgt',5)))
_SfpsMcastIPRIBOrigin_Type.__name__=_C
_SfpsMcastIPRIBOrigin_Object=MibTableColumn
sfpsMcastIPRIBOrigin=_SfpsMcastIPRIBOrigin_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1,2),_SfpsMcastIPRIBOrigin_Type())
sfpsMcastIPRIBOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBOrigin.setStatus(_A)
class _SfpsMcastIPRIBInclusion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SfpsMcastIPRIBInclusion_Type.__name__=_C
_SfpsMcastIPRIBInclusion_Object=MibTableColumn
sfpsMcastIPRIBInclusion=_SfpsMcastIPRIBInclusion_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1,3),_SfpsMcastIPRIBInclusion_Type())
sfpsMcastIPRIBInclusion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBInclusion.setStatus(_A)
_SfpsMcastIPRIBRcvPorts_Type=OctetString
_SfpsMcastIPRIBRcvPorts_Object=MibTableColumn
sfpsMcastIPRIBRcvPorts=_SfpsMcastIPRIBRcvPorts_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1,4),_SfpsMcastIPRIBRcvPorts_Type())
sfpsMcastIPRIBRcvPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBRcvPorts.setStatus(_A)
_SfpsMcastIPRIBAge_Type=Integer32
_SfpsMcastIPRIBAge_Object=MibTableColumn
sfpsMcastIPRIBAge=_SfpsMcastIPRIBAge_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,1,1,5),_SfpsMcastIPRIBAge_Type())
sfpsMcastIPRIBAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBAge.setStatus(_A)
_SfpsMcastIPRIBApiGroup_Type=IpAddress
_SfpsMcastIPRIBApiGroup_Object=MibScalar
sfpsMcastIPRIBApiGroup=_SfpsMcastIPRIBApiGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,2,1),_SfpsMcastIPRIBApiGroup_Type())
sfpsMcastIPRIBApiGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBApiGroup.setStatus(_A)
_SfpsMcastIPRIBApiPort_Type=Integer32
_SfpsMcastIPRIBApiPort_Object=MibScalar
sfpsMcastIPRIBApiPort=_SfpsMcastIPRIBApiPort_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,2,2),_SfpsMcastIPRIBApiPort_Type())
sfpsMcastIPRIBApiPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBApiPort.setStatus(_A)
class _SfpsMcastIPRIBApiVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('includePort',1),(_L,2),('excludePort',3),(_M,4)))
_SfpsMcastIPRIBApiVerb_Type.__name__=_C
_SfpsMcastIPRIBApiVerb_Object=MibScalar
sfpsMcastIPRIBApiVerb=_SfpsMcastIPRIBApiVerb_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,3,2,3),_SfpsMcastIPRIBApiVerb_Type())
sfpsMcastIPRIBApiVerb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPRIBApiVerb.setStatus(_A)
_SfpsMcastIPSIBTable_Object=MibTable
sfpsMcastIPSIBTable=_SfpsMcastIPSIBTable_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1))
if mibBuilder.loadTexts:sfpsMcastIPSIBTable.setStatus(_A)
_SfpsMcastIPSIBEntry_Object=MibTableRow
sfpsMcastIPSIBEntry=_SfpsMcastIPSIBEntry_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1,1))
sfpsMcastIPSIBEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:sfpsMcastIPSIBEntry.setStatus(_A)
_SfpsMcastIPSIBGroup_Type=IpAddress
_SfpsMcastIPSIBGroup_Object=MibTableColumn
sfpsMcastIPSIBGroup=_SfpsMcastIPSIBGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1,1,1),_SfpsMcastIPSIBGroup_Type())
sfpsMcastIPSIBGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPSIBGroup.setStatus(_A)
_SfpsMcastIPSIBSender_Type=OctetString
_SfpsMcastIPSIBSender_Object=MibTableColumn
sfpsMcastIPSIBSender=_SfpsMcastIPSIBSender_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1,1,2),_SfpsMcastIPSIBSender_Type())
sfpsMcastIPSIBSender.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPSIBSender.setStatus(_A)
class _SfpsMcastIPSIBInclusion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SfpsMcastIPSIBInclusion_Type.__name__=_C
_SfpsMcastIPSIBInclusion_Object=MibTableColumn
sfpsMcastIPSIBInclusion=_SfpsMcastIPSIBInclusion_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1,1,3),_SfpsMcastIPSIBInclusion_Type())
sfpsMcastIPSIBInclusion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPSIBInclusion.setStatus(_A)
_SfpsMcastIPSIBAge_Type=Integer32
_SfpsMcastIPSIBAge_Object=MibTableColumn
sfpsMcastIPSIBAge=_SfpsMcastIPSIBAge_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,1,1,4),_SfpsMcastIPSIBAge_Type())
sfpsMcastIPSIBAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastIPSIBAge.setStatus(_A)
_SfpsMcastIPSibApiGroup_Type=IpAddress
_SfpsMcastIPSibApiGroup_Object=MibScalar
sfpsMcastIPSibApiGroup=_SfpsMcastIPSibApiGroup_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,2,1),_SfpsMcastIPSibApiGroup_Type())
sfpsMcastIPSibApiGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPSibApiGroup.setStatus(_A)
_SfpsMcastIPSibApiSender_Type=SfpsAddress
_SfpsMcastIPSibApiSender_Object=MibScalar
sfpsMcastIPSibApiSender=_SfpsMcastIPSibApiSender_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,2,2),_SfpsMcastIPSibApiSender_Type())
sfpsMcastIPSibApiSender.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPSibApiSender.setStatus(_A)
class _SfpsMcastIPSibApiVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('includeSender',1),(_L,2),('excludeSender',3),(_M,4),('reset',5)))
_SfpsMcastIPSibApiVerb_Type.__name__=_C
_SfpsMcastIPSibApiVerb_Object=MibScalar
sfpsMcastIPSibApiVerb=_SfpsMcastIPSibApiVerb_Object((1,3,6,1,4,1,52,4,2,4,2,5,2,4,2,3),_SfpsMcastIPSibApiVerb_Type())
sfpsMcastIPSibApiVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsMcastIPSibApiVerb.setStatus(_A)
_SfpsMcastConfigApiSenderTableSize_Type=Integer32
_SfpsMcastConfigApiSenderTableSize_Object=MibScalar
sfpsMcastConfigApiSenderTableSize=_SfpsMcastConfigApiSenderTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,1),_SfpsMcastConfigApiSenderTableSize_Type())
sfpsMcastConfigApiSenderTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiSenderTableSize.setStatus(_A)
_SfpsMcastConfigApiMaxNonFilters_Type=Integer32
_SfpsMcastConfigApiMaxNonFilters_Object=MibScalar
sfpsMcastConfigApiMaxNonFilters=_SfpsMcastConfigApiMaxNonFilters_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,2),_SfpsMcastConfigApiMaxNonFilters_Type())
sfpsMcastConfigApiMaxNonFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiMaxNonFilters.setStatus(_A)
_SfpsMcastConfigApiRDRetryBuffs_Type=Integer32
_SfpsMcastConfigApiRDRetryBuffs_Object=MibScalar
sfpsMcastConfigApiRDRetryBuffs=_SfpsMcastConfigApiRDRetryBuffs_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,3),_SfpsMcastConfigApiRDRetryBuffs_Type())
sfpsMcastConfigApiRDRetryBuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiRDRetryBuffs.setStatus(_A)
_SfpsMcastConfigApiRDPktBuffs_Type=Integer32
_SfpsMcastConfigApiRDPktBuffs_Object=MibScalar
sfpsMcastConfigApiRDPktBuffs=_SfpsMcastConfigApiRDPktBuffs_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,4),_SfpsMcastConfigApiRDPktBuffs_Type())
sfpsMcastConfigApiRDPktBuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiRDPktBuffs.setStatus(_A)
_SfpsMcastConfigApiPendingMaps_Type=Integer32
_SfpsMcastConfigApiPendingMaps_Object=MibScalar
sfpsMcastConfigApiPendingMaps=_SfpsMcastConfigApiPendingMaps_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,5),_SfpsMcastConfigApiPendingMaps_Type())
sfpsMcastConfigApiPendingMaps.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiPendingMaps.setStatus(_A)
_SfpsMcastConfigApiSndrAgeOut_Type=Integer32
_SfpsMcastConfigApiSndrAgeOut_Object=MibScalar
sfpsMcastConfigApiSndrAgeOut=_SfpsMcastConfigApiSndrAgeOut_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,6),_SfpsMcastConfigApiSndrAgeOut_Type())
sfpsMcastConfigApiSndrAgeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiSndrAgeOut.setStatus(_A)
_SfpsMcastConfigApiRefreshInterval_Type=Integer32
_SfpsMcastConfigApiRefreshInterval_Object=MibScalar
sfpsMcastConfigApiRefreshInterval=_SfpsMcastConfigApiRefreshInterval_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,7),_SfpsMcastConfigApiRefreshInterval_Type())
sfpsMcastConfigApiRefreshInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiRefreshInterval.setStatus(_A)
_SfpsMcastConfigApiSndersPerAncmt_Type=Integer32
_SfpsMcastConfigApiSndersPerAncmt_Object=MibScalar
sfpsMcastConfigApiSndersPerAncmt=_SfpsMcastConfigApiSndersPerAncmt_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,8),_SfpsMcastConfigApiSndersPerAncmt_Type())
sfpsMcastConfigApiSndersPerAncmt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiSndersPerAncmt.setStatus(_A)
_SfpsMcastConfigApiDebugLog_Type=Integer32
_SfpsMcastConfigApiDebugLog_Object=MibScalar
sfpsMcastConfigApiDebugLog=_SfpsMcastConfigApiDebugLog_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,9),_SfpsMcastConfigApiDebugLog_Type())
sfpsMcastConfigApiDebugLog.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiDebugLog.setStatus(_A)
_SfpsMcastConfigApiStaticTblSize_Type=Integer32
_SfpsMcastConfigApiStaticTblSize_Object=MibScalar
sfpsMcastConfigApiStaticTblSize=_SfpsMcastConfigApiStaticTblSize_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,10),_SfpsMcastConfigApiStaticTblSize_Type())
sfpsMcastConfigApiStaticTblSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiStaticTblSize.setStatus(_A)
_SfpsMcastConfigApiMcribSize_Type=Integer32
_SfpsMcastConfigApiMcribSize_Object=MibScalar
sfpsMcastConfigApiMcribSize=_SfpsMcastConfigApiMcribSize_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,11),_SfpsMcastConfigApiMcribSize_Type())
sfpsMcastConfigApiMcribSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiMcribSize.setStatus(_A)
class _SfpsMcastConfigApiMcastMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('doNoVlanChecking',1),('doSomeVlanChecking',2),('checkAll',3)))
_SfpsMcastConfigApiMcastMode_Type.__name__=_C
_SfpsMcastConfigApiMcastMode_Object=MibScalar
sfpsMcastConfigApiMcastMode=_SfpsMcastConfigApiMcastMode_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,12),_SfpsMcastConfigApiMcastMode_Type())
sfpsMcastConfigApiMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiMcastMode.setStatus(_A)
_SfpsMcastConfigApiRemapDelay_Type=Integer32
_SfpsMcastConfigApiRemapDelay_Object=MibScalar
sfpsMcastConfigApiRemapDelay=_SfpsMcastConfigApiRemapDelay_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,13),_SfpsMcastConfigApiRemapDelay_Type())
sfpsMcastConfigApiRemapDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiRemapDelay.setStatus(_A)
_SfpsMcastConfigApiQHighLimit_Type=Integer32
_SfpsMcastConfigApiQHighLimit_Object=MibScalar
sfpsMcastConfigApiQHighLimit=_SfpsMcastConfigApiQHighLimit_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,14),_SfpsMcastConfigApiQHighLimit_Type())
sfpsMcastConfigApiQHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiQHighLimit.setStatus(_A)
_SfpsMcastConfigApiQLowLimit_Type=Integer32
_SfpsMcastConfigApiQLowLimit_Object=MibScalar
sfpsMcastConfigApiQLowLimit=_SfpsMcastConfigApiQLowLimit_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,15),_SfpsMcastConfigApiQLowLimit_Type())
sfpsMcastConfigApiQLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiQLowLimit.setStatus(_A)
_SfpsMcastConfigApiDynamicQuery_Type=Integer32
_SfpsMcastConfigApiDynamicQuery_Object=MibScalar
sfpsMcastConfigApiDynamicQuery=_SfpsMcastConfigApiDynamicQuery_Object((1,3,6,1,4,1,52,4,2,4,2,5,4,1,16),_SfpsMcastConfigApiDynamicQuery_Type())
sfpsMcastConfigApiDynamicQuery.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMcastConfigApiDynamicQuery.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SfpsAddress':SfpsAddress,'sfpsMcastCnxDestination':sfpsMcastCnxDestination,'sfpsMcastCnxSource':sfpsMcastCnxSource,'sfpsMcastCnxSenderSw':sfpsMcastCnxSenderSw,'sfpsMcastCnxInPort':sfpsMcastCnxInPort,'sfpsMcastCnxOutPorts':sfpsMcastCnxOutPorts,'sfpsMcastCnxGroup':sfpsMcastCnxGroup,'sfpsMcastCnxTTL':sfpsMcastCnxTTL,'sfpsMcastCnxAge':sfpsMcastCnxAge,'sfpsMcastCnxStatus':sfpsMcastCnxStatus,'sfpsMcastCnxNextSw':sfpsMcastCnxNextSw,'sfpsMcastCnxAPIDestination':sfpsMcastCnxAPIDestination,'sfpsMcastCnxAPISource':sfpsMcastCnxAPISource,'sfpsMcastCnxAPISenderSw':sfpsMcastCnxAPISenderSw,'sfpsMcastCnxAPIInPort':sfpsMcastCnxAPIInPort,'sfpsMcastCnxAPIOutPort':sfpsMcastCnxAPIOutPort,'sfpsMcastCnxAPIGroup':sfpsMcastCnxAPIGroup,'sfpsMcastCnxAPITTL':sfpsMcastCnxAPITTL,'sfpsMcastCnxAPIVerb':sfpsMcastCnxAPIVerb,'sfpsMcastCnxAPIFilters':sfpsMcastCnxAPIFilters,'sfpsMcastCnxAPINonFilters':sfpsMcastCnxAPINonFilters,'sfpsMcastIPRouterTable':sfpsMcastIPRouterTable,'sfpsMcastIPRouterEntry':sfpsMcastIPRouterEntry,_H:sfpsMcastIPRouterIfNum,'sfpsMcastIPRouterVlanId':sfpsMcastIPRouterVlanId,'sfpsMcastIPRouterRouterIP':sfpsMcastIPRouterRouterIP,'sfpsMcastIPRouterTTL':sfpsMcastIPRouterTTL,'sfpsMcastIPRouterAPIVerb':sfpsMcastIPRouterAPIVerb,'sfpsMcastIPRouterAPIIFNum':sfpsMcastIPRouterAPIIFNum,'sfpsMcastIPRouterAPIRouterIP':sfpsMcastIPRouterAPIRouterIP,'sfpsMcastIPRouterAPITTLScope':sfpsMcastIPRouterAPITTLScope,'sfpsMcastIPRouterAPIVlanId':sfpsMcastIPRouterAPIVlanId,'sfpsMcastIPRIBTable':sfpsMcastIPRIBTable,'sfpsMcastIPRIBEntry':sfpsMcastIPRIBEntry,_I:sfpsMcastIPRIBGroup,'sfpsMcastIPRIBOrigin':sfpsMcastIPRIBOrigin,'sfpsMcastIPRIBInclusion':sfpsMcastIPRIBInclusion,'sfpsMcastIPRIBRcvPorts':sfpsMcastIPRIBRcvPorts,'sfpsMcastIPRIBAge':sfpsMcastIPRIBAge,'sfpsMcastIPRIBApiGroup':sfpsMcastIPRIBApiGroup,'sfpsMcastIPRIBApiPort':sfpsMcastIPRIBApiPort,'sfpsMcastIPRIBApiVerb':sfpsMcastIPRIBApiVerb,'sfpsMcastIPSIBTable':sfpsMcastIPSIBTable,'sfpsMcastIPSIBEntry':sfpsMcastIPSIBEntry,_N:sfpsMcastIPSIBGroup,_O:sfpsMcastIPSIBSender,'sfpsMcastIPSIBInclusion':sfpsMcastIPSIBInclusion,'sfpsMcastIPSIBAge':sfpsMcastIPSIBAge,'sfpsMcastIPSibApiGroup':sfpsMcastIPSibApiGroup,'sfpsMcastIPSibApiSender':sfpsMcastIPSibApiSender,'sfpsMcastIPSibApiVerb':sfpsMcastIPSibApiVerb,'sfpsMcastConfigApiSenderTableSize':sfpsMcastConfigApiSenderTableSize,'sfpsMcastConfigApiMaxNonFilters':sfpsMcastConfigApiMaxNonFilters,'sfpsMcastConfigApiRDRetryBuffs':sfpsMcastConfigApiRDRetryBuffs,'sfpsMcastConfigApiRDPktBuffs':sfpsMcastConfigApiRDPktBuffs,'sfpsMcastConfigApiPendingMaps':sfpsMcastConfigApiPendingMaps,'sfpsMcastConfigApiSndrAgeOut':sfpsMcastConfigApiSndrAgeOut,'sfpsMcastConfigApiRefreshInterval':sfpsMcastConfigApiRefreshInterval,'sfpsMcastConfigApiSndersPerAncmt':sfpsMcastConfigApiSndersPerAncmt,'sfpsMcastConfigApiDebugLog':sfpsMcastConfigApiDebugLog,'sfpsMcastConfigApiStaticTblSize':sfpsMcastConfigApiStaticTblSize,'sfpsMcastConfigApiMcribSize':sfpsMcastConfigApiMcribSize,'sfpsMcastConfigApiMcastMode':sfpsMcastConfigApiMcastMode,'sfpsMcastConfigApiRemapDelay':sfpsMcastConfigApiRemapDelay,'sfpsMcastConfigApiQHighLimit':sfpsMcastConfigApiQHighLimit,'sfpsMcastConfigApiQLowLimit':sfpsMcastConfigApiQLowLimit,'sfpsMcastConfigApiDynamicQuery':sfpsMcastConfigApiDynamicQuery})