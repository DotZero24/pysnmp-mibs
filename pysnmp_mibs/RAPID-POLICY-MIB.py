_H='rsPolicyID'
_G='rsPolicyToTunnelTunnelID'
_F='rsPolicyToTunnelPolicyID'
_E='Integer32'
_D='OctetString'
_C='RAPID-POLICY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rsPolicyMIB=ModuleIdentity((1,3,6,1,4,1,4355,4))
if mibBuilder.loadTexts:rsPolicyMIB.setRevisions(('2001-05-21 12:00','2002-11-01 12:00'))
_RsPolicyToTunnel_ObjectIdentity=ObjectIdentity
rsPolicyToTunnel=_RsPolicyToTunnel_ObjectIdentity((1,3,6,1,4,1,4355,4,1))
if mibBuilder.loadTexts:rsPolicyToTunnel.setStatus(_A)
_RsPolicyToTunnelNum_Type=Unsigned32
_RsPolicyToTunnelNum_Object=MibScalar
rsPolicyToTunnelNum=_RsPolicyToTunnelNum_Object((1,3,6,1,4,1,4355,4,1,1),_RsPolicyToTunnelNum_Type())
rsPolicyToTunnelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyToTunnelNum.setStatus(_A)
_RsPolicyToTunnelTable_Object=MibTable
rsPolicyToTunnelTable=_RsPolicyToTunnelTable_Object((1,3,6,1,4,1,4355,4,1,2))
if mibBuilder.loadTexts:rsPolicyToTunnelTable.setStatus(_A)
_RsPolicyToTunnelEntry_Object=MibTableRow
rsPolicyToTunnelEntry=_RsPolicyToTunnelEntry_Object((1,3,6,1,4,1,4355,4,1,2,1))
rsPolicyToTunnelEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rsPolicyToTunnelEntry.setStatus(_A)
_RsPolicyToTunnelPolicyID_Type=Integer32
_RsPolicyToTunnelPolicyID_Object=MibTableColumn
rsPolicyToTunnelPolicyID=_RsPolicyToTunnelPolicyID_Object((1,3,6,1,4,1,4355,4,1,2,1,1),_RsPolicyToTunnelPolicyID_Type())
rsPolicyToTunnelPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyToTunnelPolicyID.setStatus(_A)
_RsPolicyToTunnelTunnelID_Type=Integer32
_RsPolicyToTunnelTunnelID_Object=MibTableColumn
rsPolicyToTunnelTunnelID=_RsPolicyToTunnelTunnelID_Object((1,3,6,1,4,1,4355,4,1,2,1,2),_RsPolicyToTunnelTunnelID_Type())
rsPolicyToTunnelTunnelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyToTunnelTunnelID.setStatus(_A)
_RsPolicyStatistics_ObjectIdentity=ObjectIdentity
rsPolicyStatistics=_RsPolicyStatistics_ObjectIdentity((1,3,6,1,4,1,4355,4,2))
if mibBuilder.loadTexts:rsPolicyStatistics.setStatus(_A)
_RsPolicyTableNum_Type=Unsigned32
_RsPolicyTableNum_Object=MibScalar
rsPolicyTableNum=_RsPolicyTableNum_Object((1,3,6,1,4,1,4355,4,2,1),_RsPolicyTableNum_Type())
rsPolicyTableNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyTableNum.setStatus(_A)
_RsPolicyTable_Object=MibTable
rsPolicyTable=_RsPolicyTable_Object((1,3,6,1,4,1,4355,4,2,2))
if mibBuilder.loadTexts:rsPolicyTable.setStatus(_A)
_RsPolicyEntry_Object=MibTableRow
rsPolicyEntry=_RsPolicyEntry_Object((1,3,6,1,4,1,4355,4,2,2,1))
rsPolicyEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:rsPolicyEntry.setStatus(_A)
_RsPolicyID_Type=Integer32
_RsPolicyID_Object=MibTableColumn
rsPolicyID=_RsPolicyID_Object((1,3,6,1,4,1,4355,4,2,2,1,1),_RsPolicyID_Type())
rsPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyID.setStatus(_A)
class _RsPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RsPolicyName_Type.__name__=_D
_RsPolicyName_Object=MibTableColumn
rsPolicyName=_RsPolicyName_Object((1,3,6,1,4,1,4355,4,2,2,1,2),_RsPolicyName_Type())
rsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyName.setStatus(_A)
_RsPolicyBytes_Type=Counter64
_RsPolicyBytes_Object=MibTableColumn
rsPolicyBytes=_RsPolicyBytes_Object((1,3,6,1,4,1,4355,4,2,2,1,3),_RsPolicyBytes_Type())
rsPolicyBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyBytes.setStatus(_A)
_RsPolicyPackets_Type=Counter64
_RsPolicyPackets_Object=MibTableColumn
rsPolicyPackets=_RsPolicyPackets_Object((1,3,6,1,4,1,4355,4,2,2,1,4),_RsPolicyPackets_Type())
rsPolicyPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyPackets.setStatus(_A)
_RsPolicyIpsecDecryptErr_Type=Counter64
_RsPolicyIpsecDecryptErr_Object=MibTableColumn
rsPolicyIpsecDecryptErr=_RsPolicyIpsecDecryptErr_Object((1,3,6,1,4,1,4355,4,2,2,1,5),_RsPolicyIpsecDecryptErr_Type())
rsPolicyIpsecDecryptErr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecDecryptErr.setStatus(_A)
_RsPolicyIpsecAuthErr_Type=Counter64
_RsPolicyIpsecAuthErr_Object=MibTableColumn
rsPolicyIpsecAuthErr=_RsPolicyIpsecAuthErr_Object((1,3,6,1,4,1,4355,4,2,2,1,6),_RsPolicyIpsecAuthErr_Type())
rsPolicyIpsecAuthErr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecAuthErr.setStatus(_A)
_RsPolicyIpsecReplayErr_Type=Counter64
_RsPolicyIpsecReplayErr_Object=MibTableColumn
rsPolicyIpsecReplayErr=_RsPolicyIpsecReplayErr_Object((1,3,6,1,4,1,4355,4,2,2,1,7),_RsPolicyIpsecReplayErr_Type())
rsPolicyIpsecReplayErr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecReplayErr.setStatus(_A)
_RsPolicyIpsecPadErr_Type=Counter64
_RsPolicyIpsecPadErr_Object=MibTableColumn
rsPolicyIpsecPadErr=_RsPolicyIpsecPadErr_Object((1,3,6,1,4,1,4355,4,2,2,1,8),_RsPolicyIpsecPadErr_Type())
rsPolicyIpsecPadErr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecPadErr.setStatus(_A)
_RsPolicyIpsecPolicyErr_Type=Counter64
_RsPolicyIpsecPolicyErr_Object=MibTableColumn
rsPolicyIpsecPolicyErr=_RsPolicyIpsecPolicyErr_Object((1,3,6,1,4,1,4355,4,2,2,1,9),_RsPolicyIpsecPolicyErr_Type())
rsPolicyIpsecPolicyErr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecPolicyErr.setStatus(_A)
_RsPolicyFwDisc_Type=Counter64
_RsPolicyFwDisc_Object=MibTableColumn
rsPolicyFwDisc=_RsPolicyFwDisc_Object((1,3,6,1,4,1,4355,4,2,2,1,10),_RsPolicyFwDisc_Type())
rsPolicyFwDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyFwDisc.setStatus(_A)
_RsPolicyOtherDisc_Type=Counter64
_RsPolicyOtherDisc_Object=MibTableColumn
rsPolicyOtherDisc=_RsPolicyOtherDisc_Object((1,3,6,1,4,1,4355,4,2,2,1,11),_RsPolicyOtherDisc_Type())
rsPolicyOtherDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyOtherDisc.setStatus(_A)
_RsPolicyActiveStreams_Type=Counter64
_RsPolicyActiveStreams_Object=MibTableColumn
rsPolicyActiveStreams=_RsPolicyActiveStreams_Object((1,3,6,1,4,1,4355,4,2,2,1,12),_RsPolicyActiveStreams_Type())
rsPolicyActiveStreams.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyActiveStreams.setStatus(_A)
_RsPolicyIpsecDisc_Type=Counter64
_RsPolicyIpsecDisc_Object=MibTableColumn
rsPolicyIpsecDisc=_RsPolicyIpsecDisc_Object((1,3,6,1,4,1,4355,4,2,2,1,13),_RsPolicyIpsecDisc_Type())
rsPolicyIpsecDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyIpsecDisc.setStatus(_A)
_RsPolicyDisc_Type=Counter64
_RsPolicyDisc_Object=MibTableColumn
rsPolicyDisc=_RsPolicyDisc_Object((1,3,6,1,4,1,4355,4,2,2,1,14),_RsPolicyDisc_Type())
rsPolicyDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyDisc.setStatus(_A)
_RsPolicyNumTunl_Type=Counter64
_RsPolicyNumTunl_Object=MibTableColumn
rsPolicyNumTunl=_RsPolicyNumTunl_Object((1,3,6,1,4,1,4355,4,2,2,1,15),_RsPolicyNumTunl_Type())
rsPolicyNumTunl.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyNumTunl.setStatus(_A)
_RsPolicySingleCntrNum_Type=Counter64
_RsPolicySingleCntrNum_Object=MibTableColumn
rsPolicySingleCntrNum=_RsPolicySingleCntrNum_Object((1,3,6,1,4,1,4355,4,2,2,1,16),_RsPolicySingleCntrNum_Type())
rsPolicySingleCntrNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicySingleCntrNum.setStatus(_A)
class _RsPolicyLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_RsPolicyLogging_Type.__name__=_E
_RsPolicyLogging_Object=MibTableColumn
rsPolicyLogging=_RsPolicyLogging_Object((1,3,6,1,4,1,4355,4,2,2,1,17),_RsPolicyLogging_Type())
rsPolicyLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:rsPolicyLogging.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rsPolicyMIB':rsPolicyMIB,'rsPolicyToTunnel':rsPolicyToTunnel,'rsPolicyToTunnelNum':rsPolicyToTunnelNum,'rsPolicyToTunnelTable':rsPolicyToTunnelTable,'rsPolicyToTunnelEntry':rsPolicyToTunnelEntry,_F:rsPolicyToTunnelPolicyID,_G:rsPolicyToTunnelTunnelID,'rsPolicyStatistics':rsPolicyStatistics,'rsPolicyTableNum':rsPolicyTableNum,'rsPolicyTable':rsPolicyTable,'rsPolicyEntry':rsPolicyEntry,_H:rsPolicyID,'rsPolicyName':rsPolicyName,'rsPolicyBytes':rsPolicyBytes,'rsPolicyPackets':rsPolicyPackets,'rsPolicyIpsecDecryptErr':rsPolicyIpsecDecryptErr,'rsPolicyIpsecAuthErr':rsPolicyIpsecAuthErr,'rsPolicyIpsecReplayErr':rsPolicyIpsecReplayErr,'rsPolicyIpsecPadErr':rsPolicyIpsecPadErr,'rsPolicyIpsecPolicyErr':rsPolicyIpsecPolicyErr,'rsPolicyFwDisc':rsPolicyFwDisc,'rsPolicyOtherDisc':rsPolicyOtherDisc,'rsPolicyActiveStreams':rsPolicyActiveStreams,'rsPolicyIpsecDisc':rsPolicyIpsecDisc,'rsPolicyDisc':rsPolicyDisc,'rsPolicyNumTunl':rsPolicyNumTunl,'rsPolicySingleCntrNum':rsPolicySingleCntrNum,'rsPolicyLogging':rsPolicyLogging})