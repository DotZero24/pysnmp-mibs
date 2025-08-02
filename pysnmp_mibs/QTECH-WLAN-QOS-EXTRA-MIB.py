_A1='qtechWlanQosPriMappingonfigGroup'
_A0='qtechWlanQosRatelimitConfigGroup'
_z='qtechWlanQosWMMEDCAConfigGroup'
_y='qtechSVPmappingAC'
_x='qtechSVPmappingStatus'
_w='qtechUserBurstRate'
_v='qtechUserAverageRate'
_u='qtechUserRatelimitStatus'
_t='qtechAPBurstRate'
_s='qtechAPAverageRate'
_r='qtechAPRatelimitStatus'
_q='qtechWlanBurstRate'
_p='qtechWlanAverageRate'
_o='qtechWlanRatelimitStatus'
_n='qtechdot11QAPEDCATableMandatory'
_m='qtechdot11QAPEDCATableMSDULifetime'
_l='qtechdot11QAPEDCATableTXOPLimit'
_k='qtechdot11QAPEDCATableAIFSN'
_j='qtechdot11QAPEDCATableCWmax'
_i='qtechdot11QAPEDCATableCWmin'
_h='qtechdot11EDCATableMandatory'
_g='qtechdot11EDCATableMSDULifetime'
_f='qtechdot11EDCATableTXOPLimit'
_e='qtechdot11EDCATableAIFSN'
_d='qtechdot11EDCATableCWmax'
_c='qtechdot11EDCATableCWmin'
_b='qtechAPdefaultDot1pTag'
_a='qtechAPdefaultDSCPTag'
_Z='qtechdscpmappingstatus'
_Y='qtechdot1pmappingstatus'
_X='qtechWlanMaxstadot1ptag'
_W='qtechWlanDefualtACnum'
_V='qtechQAPEDCAcacParam'
_U='qtechQAPEDCAcacPolicy'
_T='qtechQAPEDCAqueuedepth'
_S='qtechSMPSStatus'
_R='qtechAPSDStatus'
_Q='qtechWMMStatus'
_P='qtechUserRateLimitDirect'
_O='qtechAPRateLimitDirect'
_N='qtechdot11EDCATableIndex'
_M='qtechStaMacAddr'
_L='qtechWlanRateLimitDirect'
_K='qtechdot11QAPEDCATableIndex'
_J='not-accessible'
_I='TruthValue'
_H='qtechApCfgRadioId'
_G='qtechApgWlanId'
_F='qtechApMacAddr'
_E='QTECH-AC-MGMT-MIB'
_D='Integer32'
_C='read-write'
_B='QTECH-WLAN-QOS-EXTRA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechApCfgRadioId,qtechApMacAddr,qtechApgWlanId,qtechStaMacAddr=mibBuilder.importSymbols(_E,_H,_F,_G,_M)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
qtechWlanQosExtraMib=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,60))
if mibBuilder.loadTexts:qtechWlanQosExtraMib.setRevisions(('2009-09-08 00:00',))
_QtechWlanDeviceWMMObjects_ObjectIdentity=ObjectIdentity
qtechWlanDeviceWMMObjects=_QtechWlanDeviceWMMObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,1))
_QtechWMMStatusTable_Object=MibTable
qtechWMMStatusTable=_QtechWMMStatusTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,1,1))
if mibBuilder.loadTexts:qtechWMMStatusTable.setStatus(_A)
_QtechWMMStatusEntry_Object=MibTableRow
qtechWMMStatusEntry=_QtechWMMStatusEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,1,1,1))
qtechWMMStatusEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:qtechWMMStatusEntry.setStatus(_A)
class _QtechWMMStatus_Type(TruthValue):defaultValue=1
_QtechWMMStatus_Type.__name__=_I
_QtechWMMStatus_Object=MibTableColumn
qtechWMMStatus=_QtechWMMStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,1,1,1,1),_QtechWMMStatus_Type())
qtechWMMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWMMStatus.setStatus(_A)
class _QtechAPSDStatus_Type(TruthValue):defaultValue=1
_QtechAPSDStatus_Type.__name__=_I
_QtechAPSDStatus_Object=MibTableColumn
qtechAPSDStatus=_QtechAPSDStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,1,1,1,2),_QtechAPSDStatus_Type())
qtechAPSDStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPSDStatus.setStatus(_A)
class _QtechSMPSStatus_Type(TruthValue):defaultValue=1
_QtechSMPSStatus_Type.__name__=_I
_QtechSMPSStatus_Object=MibTableColumn
qtechSMPSStatus=_QtechSMPSStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,1,1,1,3),_QtechSMPSStatus_Type())
qtechSMPSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPSStatus.setStatus(_A)
_QtechWlanDeviceEDCAObjects_ObjectIdentity=ObjectIdentity
qtechWlanDeviceEDCAObjects=_QtechWlanDeviceEDCAObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,2))
_Qtechdot11EDCATable_Object=MibTable
qtechdot11EDCATable=_Qtechdot11EDCATable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1))
if mibBuilder.loadTexts:qtechdot11EDCATable.setStatus(_A)
_Qtechdot11EDCAEntry_Object=MibTableRow
qtechdot11EDCAEntry=_Qtechdot11EDCAEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1))
qtechdot11EDCAEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_B,_N))
if mibBuilder.loadTexts:qtechdot11EDCAEntry.setStatus(_A)
class _Qtechdot11EDCATableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Qtechdot11EDCATableIndex_Type.__name__=_D
_Qtechdot11EDCATableIndex_Object=MibTableColumn
qtechdot11EDCATableIndex=_Qtechdot11EDCATableIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,1),_Qtechdot11EDCATableIndex_Type())
qtechdot11EDCATableIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechdot11EDCATableIndex.setStatus(_A)
class _Qtechdot11EDCATableCWmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Qtechdot11EDCATableCWmin_Type.__name__=_D
_Qtechdot11EDCATableCWmin_Object=MibTableColumn
qtechdot11EDCATableCWmin=_Qtechdot11EDCATableCWmin_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,2),_Qtechdot11EDCATableCWmin_Type())
qtechdot11EDCATableCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableCWmin.setStatus(_A)
class _Qtechdot11EDCATableCWmax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Qtechdot11EDCATableCWmax_Type.__name__=_D
_Qtechdot11EDCATableCWmax_Object=MibTableColumn
qtechdot11EDCATableCWmax=_Qtechdot11EDCATableCWmax_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,3),_Qtechdot11EDCATableCWmax_Type())
qtechdot11EDCATableCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableCWmax.setStatus(_A)
class _Qtechdot11EDCATableAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_Qtechdot11EDCATableAIFSN_Type.__name__=_D
_Qtechdot11EDCATableAIFSN_Object=MibTableColumn
qtechdot11EDCATableAIFSN=_Qtechdot11EDCATableAIFSN_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,4),_Qtechdot11EDCATableAIFSN_Type())
qtechdot11EDCATableAIFSN.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableAIFSN.setStatus(_A)
class _Qtechdot11EDCATableTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Qtechdot11EDCATableTXOPLimit_Type.__name__=_D
_Qtechdot11EDCATableTXOPLimit_Object=MibTableColumn
qtechdot11EDCATableTXOPLimit=_Qtechdot11EDCATableTXOPLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,5),_Qtechdot11EDCATableTXOPLimit_Type())
qtechdot11EDCATableTXOPLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableTXOPLimit.setStatus(_A)
class _Qtechdot11EDCATableMSDULifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_Qtechdot11EDCATableMSDULifetime_Type.__name__=_D
_Qtechdot11EDCATableMSDULifetime_Object=MibTableColumn
qtechdot11EDCATableMSDULifetime=_Qtechdot11EDCATableMSDULifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,6),_Qtechdot11EDCATableMSDULifetime_Type())
qtechdot11EDCATableMSDULifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableMSDULifetime.setStatus(_A)
_Qtechdot11EDCATableMandatory_Type=TruthValue
_Qtechdot11EDCATableMandatory_Object=MibTableColumn
qtechdot11EDCATableMandatory=_Qtechdot11EDCATableMandatory_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,1,1,7),_Qtechdot11EDCATableMandatory_Type())
qtechdot11EDCATableMandatory.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11EDCATableMandatory.setStatus(_A)
_Qtechdot11QAPEDCATable_Object=MibTable
qtechdot11QAPEDCATable=_Qtechdot11QAPEDCATable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2))
if mibBuilder.loadTexts:qtechdot11QAPEDCATable.setStatus(_A)
_Qtechdot11QAPEDCAEntry_Object=MibTableRow
qtechdot11QAPEDCAEntry=_Qtechdot11QAPEDCAEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1))
qtechdot11QAPEDCAEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_B,_K))
if mibBuilder.loadTexts:qtechdot11QAPEDCAEntry.setStatus(_A)
class _Qtechdot11QAPEDCATableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Qtechdot11QAPEDCATableIndex_Type.__name__=_D
_Qtechdot11QAPEDCATableIndex_Object=MibTableColumn
qtechdot11QAPEDCATableIndex=_Qtechdot11QAPEDCATableIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,1),_Qtechdot11QAPEDCATableIndex_Type())
qtechdot11QAPEDCATableIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableIndex.setStatus(_A)
class _Qtechdot11QAPEDCATableCWmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Qtechdot11QAPEDCATableCWmin_Type.__name__=_D
_Qtechdot11QAPEDCATableCWmin_Object=MibTableColumn
qtechdot11QAPEDCATableCWmin=_Qtechdot11QAPEDCATableCWmin_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,2),_Qtechdot11QAPEDCATableCWmin_Type())
qtechdot11QAPEDCATableCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableCWmin.setStatus(_A)
class _Qtechdot11QAPEDCATableCWmax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Qtechdot11QAPEDCATableCWmax_Type.__name__=_D
_Qtechdot11QAPEDCATableCWmax_Object=MibTableColumn
qtechdot11QAPEDCATableCWmax=_Qtechdot11QAPEDCATableCWmax_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,3),_Qtechdot11QAPEDCATableCWmax_Type())
qtechdot11QAPEDCATableCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableCWmax.setStatus(_A)
class _Qtechdot11QAPEDCATableAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Qtechdot11QAPEDCATableAIFSN_Type.__name__=_D
_Qtechdot11QAPEDCATableAIFSN_Object=MibTableColumn
qtechdot11QAPEDCATableAIFSN=_Qtechdot11QAPEDCATableAIFSN_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,4),_Qtechdot11QAPEDCATableAIFSN_Type())
qtechdot11QAPEDCATableAIFSN.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableAIFSN.setStatus(_A)
class _Qtechdot11QAPEDCATableTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Qtechdot11QAPEDCATableTXOPLimit_Type.__name__=_D
_Qtechdot11QAPEDCATableTXOPLimit_Object=MibTableColumn
qtechdot11QAPEDCATableTXOPLimit=_Qtechdot11QAPEDCATableTXOPLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,5),_Qtechdot11QAPEDCATableTXOPLimit_Type())
qtechdot11QAPEDCATableTXOPLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableTXOPLimit.setStatus(_A)
class _Qtechdot11QAPEDCATableMSDULifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_Qtechdot11QAPEDCATableMSDULifetime_Type.__name__=_D
_Qtechdot11QAPEDCATableMSDULifetime_Object=MibTableColumn
qtechdot11QAPEDCATableMSDULifetime=_Qtechdot11QAPEDCATableMSDULifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,6),_Qtechdot11QAPEDCATableMSDULifetime_Type())
qtechdot11QAPEDCATableMSDULifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableMSDULifetime.setStatus(_A)
_Qtechdot11QAPEDCATableMandatory_Type=TruthValue
_Qtechdot11QAPEDCATableMandatory_Object=MibTableColumn
qtechdot11QAPEDCATableMandatory=_Qtechdot11QAPEDCATableMandatory_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,2,1,7),_Qtechdot11QAPEDCATableMandatory_Type())
qtechdot11QAPEDCATableMandatory.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot11QAPEDCATableMandatory.setStatus(_A)
_QtechWlanEDCATable_Object=MibTable
qtechWlanEDCATable=_QtechWlanEDCATable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,3))
if mibBuilder.loadTexts:qtechWlanEDCATable.setStatus(_A)
_QtechEDCAStatusEntry_Object=MibTableRow
qtechEDCAStatusEntry=_QtechEDCAStatusEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,3,1))
qtechEDCAStatusEntry.setIndexNames((0,_E,_F),(0,_E,_H),(0,_B,_K))
if mibBuilder.loadTexts:qtechEDCAStatusEntry.setStatus(_A)
class _QtechQAPEDCAqueuedepth_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_QtechQAPEDCAqueuedepth_Type.__name__=_D
_QtechQAPEDCAqueuedepth_Object=MibTableColumn
qtechQAPEDCAqueuedepth=_QtechQAPEDCAqueuedepth_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,3,1,1),_QtechQAPEDCAqueuedepth_Type())
qtechQAPEDCAqueuedepth.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQAPEDCAqueuedepth.setStatus(_A)
class _QtechQAPEDCAcacPolicy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nocac',0),('usernum-based',1),('channelutilization-based',2)))
_QtechQAPEDCAcacPolicy_Type.__name__=_D
_QtechQAPEDCAcacPolicy_Object=MibTableColumn
qtechQAPEDCAcacPolicy=_QtechQAPEDCAcacPolicy_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,3,1,2),_QtechQAPEDCAcacPolicy_Type())
qtechQAPEDCAcacPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQAPEDCAcacPolicy.setStatus(_A)
class _QtechQAPEDCAcacParam_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechQAPEDCAcacParam_Type.__name__=_D
_QtechQAPEDCAcacParam_Object=MibTableColumn
qtechQAPEDCAcacParam=_QtechQAPEDCAcacParam_Object((1,3,6,1,4,1,27514,1,1,10,2,60,2,3,1,3),_QtechQAPEDCAcacParam_Type())
qtechQAPEDCAcacParam.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQAPEDCAcacParam.setStatus(_A)
_QtechWlanDevicePrivMappingObjects_ObjectIdentity=ObjectIdentity
qtechWlanDevicePrivMappingObjects=_QtechWlanDevicePrivMappingObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,3))
_QtechWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity=ObjectIdentity
qtechWlanDevicePrivMappingWlanDefaultObjects=_QtechWlanDevicePrivMappingWlanDefaultObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,3,1))
_QtechWlanDefaultACTable_Object=MibTable
qtechWlanDefaultACTable=_QtechWlanDefaultACTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,1,1))
if mibBuilder.loadTexts:qtechWlanDefaultACTable.setStatus(_A)
_QtechWlanDefaultACEntry_Object=MibTableRow
qtechWlanDefaultACEntry=_QtechWlanDefaultACEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,1,1,1))
qtechWlanDefaultACEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:qtechWlanDefaultACEntry.setStatus(_A)
_QtechWlanDefualtACnum_Type=Integer32
_QtechWlanDefualtACnum_Object=MibTableColumn
qtechWlanDefualtACnum=_QtechWlanDefualtACnum_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,1,1,1,1),_QtechWlanDefualtACnum_Type())
qtechWlanDefualtACnum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanDefualtACnum.setStatus(_A)
_QtechWlanMaxstadot1ptag_Type=Integer32
_QtechWlanMaxstadot1ptag_Object=MibTableColumn
qtechWlanMaxstadot1ptag=_QtechWlanMaxstadot1ptag_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,1,1,1,2),_QtechWlanMaxstadot1ptag_Type())
qtechWlanMaxstadot1ptag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanMaxstadot1ptag.setStatus(_A)
_QtechWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity=ObjectIdentity
qtechWlanDevicePrivMappingAPDefaultObjects=_QtechWlanDevicePrivMappingAPDefaultObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,3,2))
_QtechPrivMappingAPstatusTable_Object=MibTable
qtechPrivMappingAPstatusTable=_QtechPrivMappingAPstatusTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,1))
if mibBuilder.loadTexts:qtechPrivMappingAPstatusTable.setStatus(_A)
_QtechAPdefaultStatusMappingEntry_Object=MibTableRow
qtechAPdefaultStatusMappingEntry=_QtechAPdefaultStatusMappingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,1,1))
qtechAPdefaultStatusMappingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qtechAPdefaultStatusMappingEntry.setStatus(_A)
class _Qtechdot1pmappingstatus_Type(Integer32):defaultValue=0
_Qtechdot1pmappingstatus_Type.__name__=_D
_Qtechdot1pmappingstatus_Object=MibTableColumn
qtechdot1pmappingstatus=_Qtechdot1pmappingstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,1,1,1),_Qtechdot1pmappingstatus_Type())
qtechdot1pmappingstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdot1pmappingstatus.setStatus(_A)
class _Qtechdscpmappingstatus_Type(Integer32):defaultValue=0
_Qtechdscpmappingstatus_Type.__name__=_D
_Qtechdscpmappingstatus_Object=MibTableColumn
qtechdscpmappingstatus=_Qtechdscpmappingstatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,1,1,2),_Qtechdscpmappingstatus_Type())
qtechdscpmappingstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechdscpmappingstatus.setStatus(_A)
_QtechPrivMappingAPDefaultTable_Object=MibTable
qtechPrivMappingAPDefaultTable=_QtechPrivMappingAPDefaultTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,2))
if mibBuilder.loadTexts:qtechPrivMappingAPDefaultTable.setStatus(_A)
_QtechPrivMappingAPDefaultEntry_Object=MibTableRow
qtechPrivMappingAPDefaultEntry=_QtechPrivMappingAPDefaultEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,2,1))
qtechPrivMappingAPDefaultEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:qtechPrivMappingAPDefaultEntry.setStatus(_A)
class _QtechAPdefaultDSCPTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_QtechAPdefaultDSCPTag_Type.__name__=_D
_QtechAPdefaultDSCPTag_Object=MibTableColumn
qtechAPdefaultDSCPTag=_QtechAPdefaultDSCPTag_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,2,1,1),_QtechAPdefaultDSCPTag_Type())
qtechAPdefaultDSCPTag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPdefaultDSCPTag.setStatus(_A)
_QtechAPdefaultDot1pTag_Type=Integer32
_QtechAPdefaultDot1pTag_Object=MibTableColumn
qtechAPdefaultDot1pTag=_QtechAPdefaultDot1pTag_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,2,2,1,2),_QtechAPdefaultDot1pTag_Type())
qtechAPdefaultDot1pTag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPdefaultDot1pTag.setStatus(_A)
_QtechWlanDevicePrivMappingTableObjects_ObjectIdentity=ObjectIdentity
qtechWlanDevicePrivMappingTableObjects=_QtechWlanDevicePrivMappingTableObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,3,3))
_QtechSVPMappingTable_Object=MibTable
qtechSVPMappingTable=_QtechSVPMappingTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,3,1))
if mibBuilder.loadTexts:qtechSVPMappingTable.setStatus(_A)
_QtechSVPMappingEntry_Object=MibTableRow
qtechSVPMappingEntry=_QtechSVPMappingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,3,1,1))
qtechSVPMappingEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:qtechSVPMappingEntry.setStatus(_A)
class _QtechSVPmappingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_QtechSVPmappingStatus_Type.__name__=_D
_QtechSVPmappingStatus_Object=MibTableColumn
qtechSVPmappingStatus=_QtechSVPmappingStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,3,1,1,1),_QtechSVPmappingStatus_Type())
qtechSVPmappingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSVPmappingStatus.setStatus(_A)
class _QtechSVPmappingAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wmmvo',1),('wmmvi',2),('wmmbe',3),('wmmbk',4)))
_QtechSVPmappingAC_Type.__name__=_D
_QtechSVPmappingAC_Object=MibTableColumn
qtechSVPmappingAC=_QtechSVPmappingAC_Object((1,3,6,1,4,1,27514,1,1,10,2,60,3,3,1,1,2),_QtechSVPmappingAC_Type())
qtechSVPmappingAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSVPmappingAC.setStatus(_A)
_QtechWlanDeviceRatelimitObjects_ObjectIdentity=ObjectIdentity
qtechWlanDeviceRatelimitObjects=_QtechWlanDeviceRatelimitObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,4))
_QtechWlanRatelimitTable_Object=MibTable
qtechWlanRatelimitTable=_QtechWlanRatelimitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1))
if mibBuilder.loadTexts:qtechWlanRatelimitTable.setStatus(_A)
_QtechWlanRatelimitEntry_Object=MibTableRow
qtechWlanRatelimitEntry=_QtechWlanRatelimitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1,1))
qtechWlanRatelimitEntry.setIndexNames((0,_E,_G),(0,_B,_L))
if mibBuilder.loadTexts:qtechWlanRatelimitEntry.setStatus(_A)
class _QtechWlanRateLimitDirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechWlanRateLimitDirect_Type.__name__=_D
_QtechWlanRateLimitDirect_Object=MibTableColumn
qtechWlanRateLimitDirect=_QtechWlanRateLimitDirect_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1,1,1),_QtechWlanRateLimitDirect_Type())
qtechWlanRateLimitDirect.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechWlanRateLimitDirect.setStatus(_A)
class _QtechWlanRatelimitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechWlanRatelimitStatus_Type.__name__=_D
_QtechWlanRatelimitStatus_Object=MibTableColumn
qtechWlanRatelimitStatus=_QtechWlanRatelimitStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1,1,2),_QtechWlanRatelimitStatus_Type())
qtechWlanRatelimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanRatelimitStatus.setStatus(_A)
_QtechWlanAverageRate_Type=Integer32
_QtechWlanAverageRate_Object=MibTableColumn
qtechWlanAverageRate=_QtechWlanAverageRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1,1,3),_QtechWlanAverageRate_Type())
qtechWlanAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanAverageRate.setStatus(_A)
_QtechWlanBurstRate_Type=Integer32
_QtechWlanBurstRate_Object=MibTableColumn
qtechWlanBurstRate=_QtechWlanBurstRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,1,1,4),_QtechWlanBurstRate_Type())
qtechWlanBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlanBurstRate.setStatus(_A)
_QtechAPRatelimitTable_Object=MibTable
qtechAPRatelimitTable=_QtechAPRatelimitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2))
if mibBuilder.loadTexts:qtechAPRatelimitTable.setStatus(_A)
_QtechAPRatelimitEntry_Object=MibTableRow
qtechAPRatelimitEntry=_QtechAPRatelimitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2,1))
qtechAPRatelimitEntry.setIndexNames((0,_E,_F),(0,_B,_O))
if mibBuilder.loadTexts:qtechAPRatelimitEntry.setStatus(_A)
class _QtechAPRateLimitDirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechAPRateLimitDirect_Type.__name__=_D
_QtechAPRateLimitDirect_Object=MibTableColumn
qtechAPRateLimitDirect=_QtechAPRateLimitDirect_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2,1,1),_QtechAPRateLimitDirect_Type())
qtechAPRateLimitDirect.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechAPRateLimitDirect.setStatus(_A)
class _QtechAPRatelimitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechAPRatelimitStatus_Type.__name__=_D
_QtechAPRatelimitStatus_Object=MibTableColumn
qtechAPRatelimitStatus=_QtechAPRatelimitStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2,1,2),_QtechAPRatelimitStatus_Type())
qtechAPRatelimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPRatelimitStatus.setStatus(_A)
_QtechAPAverageRate_Type=Integer32
_QtechAPAverageRate_Object=MibTableColumn
qtechAPAverageRate=_QtechAPAverageRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2,1,3),_QtechAPAverageRate_Type())
qtechAPAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPAverageRate.setStatus(_A)
_QtechAPBurstRate_Type=Integer32
_QtechAPBurstRate_Object=MibTableColumn
qtechAPBurstRate=_QtechAPBurstRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,2,1,4),_QtechAPBurstRate_Type())
qtechAPBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPBurstRate.setStatus(_A)
_QtechUserRatelimitTable_Object=MibTable
qtechUserRatelimitTable=_QtechUserRatelimitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3))
if mibBuilder.loadTexts:qtechUserRatelimitTable.setStatus(_A)
_QtechUserRatelimitEntry_Object=MibTableRow
qtechUserRatelimitEntry=_QtechUserRatelimitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3,1))
qtechUserRatelimitEntry.setIndexNames((0,_E,_M),(0,_B,_P),(0,_E,_G))
if mibBuilder.loadTexts:qtechUserRatelimitEntry.setStatus(_A)
class _QtechUserRateLimitDirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechUserRateLimitDirect_Type.__name__=_D
_QtechUserRateLimitDirect_Object=MibTableColumn
qtechUserRateLimitDirect=_QtechUserRateLimitDirect_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3,1,1),_QtechUserRateLimitDirect_Type())
qtechUserRateLimitDirect.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechUserRateLimitDirect.setStatus(_A)
class _QtechUserRatelimitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechUserRatelimitStatus_Type.__name__=_D
_QtechUserRatelimitStatus_Object=MibTableColumn
qtechUserRatelimitStatus=_QtechUserRatelimitStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3,1,2),_QtechUserRatelimitStatus_Type())
qtechUserRatelimitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechUserRatelimitStatus.setStatus(_A)
_QtechUserAverageRate_Type=Integer32
_QtechUserAverageRate_Object=MibTableColumn
qtechUserAverageRate=_QtechUserAverageRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3,1,3),_QtechUserAverageRate_Type())
qtechUserAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechUserAverageRate.setStatus(_A)
_QtechUserBurstRate_Type=Integer32
_QtechUserBurstRate_Object=MibTableColumn
qtechUserBurstRate=_QtechUserBurstRate_Object((1,3,6,1,4,1,27514,1,1,10,2,60,4,3,1,4),_QtechUserBurstRate_Type())
qtechUserBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechUserBurstRate.setStatus(_A)
_QtechWlanQosMIBConform_ObjectIdentity=ObjectIdentity
qtechWlanQosMIBConform=_QtechWlanQosMIBConform_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,5))
_QtechWlanQosMIBCompliances_ObjectIdentity=ObjectIdentity
qtechWlanQosMIBCompliances=_QtechWlanQosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,5,1))
_QtechWlanQosMIBGroups_ObjectIdentity=ObjectIdentity
qtechWlanQosMIBGroups=_QtechWlanQosMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,60,5,2))
qtechWlanQosWMMEDCAConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,60,5,2,1))
qtechWlanQosWMMEDCAConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:qtechWlanQosWMMEDCAConfigGroup.setStatus(_A)
qtechWlanQosRatelimitConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,60,5,2,2))
qtechWlanQosRatelimitConfigGroup.setObjects(*((_B,_L),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechWlanQosRatelimitConfigGroup.setStatus(_A)
qtechWlanQosPriMappingonfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,60,5,2,3))
qtechWlanQosPriMappingonfigGroup.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qtechWlanQosPriMappingonfigGroup.setStatus(_A)
qtechWlanQosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,60,5,1,1))
qtechWlanQosMIBCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:qtechWlanQosMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechWlanQosExtraMib':qtechWlanQosExtraMib,'qtechWlanDeviceWMMObjects':qtechWlanDeviceWMMObjects,'qtechWMMStatusTable':qtechWMMStatusTable,'qtechWMMStatusEntry':qtechWMMStatusEntry,_Q:qtechWMMStatus,_R:qtechAPSDStatus,_S:qtechSMPSStatus,'qtechWlanDeviceEDCAObjects':qtechWlanDeviceEDCAObjects,'qtechdot11EDCATable':qtechdot11EDCATable,'qtechdot11EDCAEntry':qtechdot11EDCAEntry,_N:qtechdot11EDCATableIndex,_c:qtechdot11EDCATableCWmin,_d:qtechdot11EDCATableCWmax,_e:qtechdot11EDCATableAIFSN,_f:qtechdot11EDCATableTXOPLimit,_g:qtechdot11EDCATableMSDULifetime,_h:qtechdot11EDCATableMandatory,'qtechdot11QAPEDCATable':qtechdot11QAPEDCATable,'qtechdot11QAPEDCAEntry':qtechdot11QAPEDCAEntry,_K:qtechdot11QAPEDCATableIndex,_i:qtechdot11QAPEDCATableCWmin,_j:qtechdot11QAPEDCATableCWmax,_k:qtechdot11QAPEDCATableAIFSN,_l:qtechdot11QAPEDCATableTXOPLimit,_m:qtechdot11QAPEDCATableMSDULifetime,_n:qtechdot11QAPEDCATableMandatory,'qtechWlanEDCATable':qtechWlanEDCATable,'qtechEDCAStatusEntry':qtechEDCAStatusEntry,_T:qtechQAPEDCAqueuedepth,_U:qtechQAPEDCAcacPolicy,_V:qtechQAPEDCAcacParam,'qtechWlanDevicePrivMappingObjects':qtechWlanDevicePrivMappingObjects,'qtechWlanDevicePrivMappingWlanDefaultObjects':qtechWlanDevicePrivMappingWlanDefaultObjects,'qtechWlanDefaultACTable':qtechWlanDefaultACTable,'qtechWlanDefaultACEntry':qtechWlanDefaultACEntry,_W:qtechWlanDefualtACnum,_X:qtechWlanMaxstadot1ptag,'qtechWlanDevicePrivMappingAPDefaultObjects':qtechWlanDevicePrivMappingAPDefaultObjects,'qtechPrivMappingAPstatusTable':qtechPrivMappingAPstatusTable,'qtechAPdefaultStatusMappingEntry':qtechAPdefaultStatusMappingEntry,_Y:qtechdot1pmappingstatus,_Z:qtechdscpmappingstatus,'qtechPrivMappingAPDefaultTable':qtechPrivMappingAPDefaultTable,'qtechPrivMappingAPDefaultEntry':qtechPrivMappingAPDefaultEntry,_a:qtechAPdefaultDSCPTag,_b:qtechAPdefaultDot1pTag,'qtechWlanDevicePrivMappingTableObjects':qtechWlanDevicePrivMappingTableObjects,'qtechSVPMappingTable':qtechSVPMappingTable,'qtechSVPMappingEntry':qtechSVPMappingEntry,_x:qtechSVPmappingStatus,_y:qtechSVPmappingAC,'qtechWlanDeviceRatelimitObjects':qtechWlanDeviceRatelimitObjects,'qtechWlanRatelimitTable':qtechWlanRatelimitTable,'qtechWlanRatelimitEntry':qtechWlanRatelimitEntry,_L:qtechWlanRateLimitDirect,_o:qtechWlanRatelimitStatus,_p:qtechWlanAverageRate,_q:qtechWlanBurstRate,'qtechAPRatelimitTable':qtechAPRatelimitTable,'qtechAPRatelimitEntry':qtechAPRatelimitEntry,_O:qtechAPRateLimitDirect,_r:qtechAPRatelimitStatus,_s:qtechAPAverageRate,_t:qtechAPBurstRate,'qtechUserRatelimitTable':qtechUserRatelimitTable,'qtechUserRatelimitEntry':qtechUserRatelimitEntry,_P:qtechUserRateLimitDirect,_u:qtechUserRatelimitStatus,_v:qtechUserAverageRate,_w:qtechUserBurstRate,'qtechWlanQosMIBConform':qtechWlanQosMIBConform,'qtechWlanQosMIBCompliances':qtechWlanQosMIBCompliances,'qtechWlanQosMIBCompliance':qtechWlanQosMIBCompliance,'qtechWlanQosMIBGroups':qtechWlanQosMIBGroups,_z:qtechWlanQosWMMEDCAConfigGroup,_A0:qtechWlanQosRatelimitConfigGroup,_A1:qtechWlanQosPriMappingonfigGroup})