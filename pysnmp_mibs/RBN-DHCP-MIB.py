_A9='rbnDhcpLeaseFileFailureNotifyGroup'
_A8='rbnDhcpLeaseFileFailureTrapGroup'
_A7='rbnDhcpThresholdNotifyGroup'
_A6='rbnDhcpThresholdGroup'
_A5='rbnDhcpLeaseFileFailure'
_A4='rbnDhcpRangeThresholdRisingThresholdMet'
_A3='rbnDhcpRangeThresholdFallingThresholdMet'
_A2='rbnDhcpRangeThresholdRisingLogMessage'
_A1='rbnDhcpRangeThresholdRisingSendTrap'
_A0='rbnDhcpRangeThresholdFallingLogMessage'
_z='rbnDhcpRangeThresholdFallingSendTrap'
_y='rbnDhcpRangeThresholdInuse'
_x='rbnDhcpRangeThresholdSize'
_w='rbnDhcpRangeThresholdAddr'
_v='rbnDhcpRangeThresholdInterfaceIdx'
_u='rbnDhcpIntfThresholdName'
_t='Integer32'
_s='rbnDhcpRangeThresholdNotifyGroup'
_r='rbnDhcpCtxThresholdNotifyGroup'
_q='rbnDhcpIntfThresholdNotifyGroup'
_p='rbnDhcpRangeThresholdGroup'
_o='rbnDhcpCtxThresholdGroup'
_n='rbnDhcpIntfThresholdGroup'
_m='rbnDhcpCtxThresholdRisingThresholdMet'
_l='rbnDhcpCtxThresholdFallingThresholdMet'
_k='rbnDhcpIntfThresholdRisingThresholdMet'
_j='rbnDhcpIntfThresholdFallingThresholdMet'
_i='rbnDhcpLeaseFileErrorType'
_h='rbnDhcpLeaseFileStorageSlot'
_g='rbnDhcpRangeThresholdRisingThreshold'
_f='rbnDhcpRangeThresholdFallingThreshold'
_e='rbnDhcpCtxThresholdRisingLogMessage'
_d='rbnDhcpCtxThresholdRisingSendTrap'
_c='rbnDhcpCtxThresholdFallingLogMessage'
_b='rbnDhcpCtxThresholdFallingSendTrap'
_a='rbnDhcpCtxThresholdInuse'
_Z='rbnDhcpCtxThresholdSize'
_Y='rbnDhcpIntfThresholdRisingLogMessage'
_X='rbnDhcpIntfThresholdRisingSendTrap'
_W='rbnDhcpIntfThresholdFallingLogMessage'
_V='rbnDhcpIntfThresholdFallingSendTrap'
_U='rbnDhcpIntfThresholdInuse'
_T='rbnDhcpIntfThresholdSize'
_S='accessible-for-notify'
_R='not-accessible'
_Q='rbnDhcpRangeThresholdAvailable'
_P='rbnDhcpRangeThresholdInterfaceName'
_O='rbnDhcpRangeThresholdContextName'
_N='rbnDhcpRangeThresholdEndAddr'
_M='rbnDhcpCtxThresholdRisingThreshold'
_L='rbnDhcpCtxThresholdFallingThreshold'
_K='rbnDhcpIntfThresholdRisingThreshold'
_J='rbnDhcpIntfThresholdFallingThreshold'
_I='rbnDhcpIntfThresholdContextName'
_H='rbnDhcpCtxThresholdAvailable'
_G='rbnDhcpCtxThresholdName'
_F='rbnDhcpIntfThresholdAvailable'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='RBN-DHCP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnSlot,=mibBuilder.importSymbols('RBN-TC','RbnSlot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_t,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rbnDhcpMib=ModuleIdentity((1,3,6,1,4,1,2352,2,30))
if mibBuilder.loadTexts:rbnDhcpMib.setRevisions(('2010-03-10 17:00','2005-10-14 17:00','2004-05-03 17:00'))
_RbnDhcpMIBNotifications_ObjectIdentity=ObjectIdentity
rbnDhcpMIBNotifications=_RbnDhcpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,30,0))
_RbnDhcpMIBObjects_ObjectIdentity=ObjectIdentity
rbnDhcpMIBObjects=_RbnDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,30,1))
_RbnDhcpIntfThresholdTable_Object=MibTable
rbnDhcpIntfThresholdTable=_RbnDhcpIntfThresholdTable_Object((1,3,6,1,4,1,2352,2,30,1,1))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdTable.setStatus(_B)
_RbnDhcpIntfThresholdEntry_Object=MibTableRow
rbnDhcpIntfThresholdEntry=_RbnDhcpIntfThresholdEntry_Object((1,3,6,1,4,1,2352,2,30,1,1,1))
rbnDhcpIntfThresholdEntry.setIndexNames((1,_A,_u))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdEntry.setStatus(_B)
class _RbnDhcpIntfThresholdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_RbnDhcpIntfThresholdName_Type.__name__=_E
_RbnDhcpIntfThresholdName_Object=MibTableColumn
rbnDhcpIntfThresholdName=_RbnDhcpIntfThresholdName_Object((1,3,6,1,4,1,2352,2,30,1,1,1,1),_RbnDhcpIntfThresholdName_Type())
rbnDhcpIntfThresholdName.setMaxAccess(_R)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdName.setStatus(_B)
class _RbnDhcpIntfThresholdContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnDhcpIntfThresholdContextName_Type.__name__=_E
_RbnDhcpIntfThresholdContextName_Object=MibTableColumn
rbnDhcpIntfThresholdContextName=_RbnDhcpIntfThresholdContextName_Object((1,3,6,1,4,1,2352,2,30,1,1,1,2),_RbnDhcpIntfThresholdContextName_Type())
rbnDhcpIntfThresholdContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdContextName.setStatus(_B)
_RbnDhcpIntfThresholdSize_Type=Unsigned32
_RbnDhcpIntfThresholdSize_Object=MibTableColumn
rbnDhcpIntfThresholdSize=_RbnDhcpIntfThresholdSize_Object((1,3,6,1,4,1,2352,2,30,1,1,1,3),_RbnDhcpIntfThresholdSize_Type())
rbnDhcpIntfThresholdSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdSize.setStatus(_B)
_RbnDhcpIntfThresholdAvailable_Type=Unsigned32
_RbnDhcpIntfThresholdAvailable_Object=MibTableColumn
rbnDhcpIntfThresholdAvailable=_RbnDhcpIntfThresholdAvailable_Object((1,3,6,1,4,1,2352,2,30,1,1,1,4),_RbnDhcpIntfThresholdAvailable_Type())
rbnDhcpIntfThresholdAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdAvailable.setStatus(_B)
_RbnDhcpIntfThresholdInuse_Type=Unsigned32
_RbnDhcpIntfThresholdInuse_Object=MibTableColumn
rbnDhcpIntfThresholdInuse=_RbnDhcpIntfThresholdInuse_Object((1,3,6,1,4,1,2352,2,30,1,1,1,5),_RbnDhcpIntfThresholdInuse_Type())
rbnDhcpIntfThresholdInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdInuse.setStatus(_B)
class _RbnDhcpIntfThresholdFallingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpIntfThresholdFallingThreshold_Type.__name__=_D
_RbnDhcpIntfThresholdFallingThreshold_Object=MibTableColumn
rbnDhcpIntfThresholdFallingThreshold=_RbnDhcpIntfThresholdFallingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,1,1,6),_RbnDhcpIntfThresholdFallingThreshold_Type())
rbnDhcpIntfThresholdFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdFallingThreshold.setStatus(_B)
_RbnDhcpIntfThresholdFallingSendTrap_Type=TruthValue
_RbnDhcpIntfThresholdFallingSendTrap_Object=MibTableColumn
rbnDhcpIntfThresholdFallingSendTrap=_RbnDhcpIntfThresholdFallingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,1,1,7),_RbnDhcpIntfThresholdFallingSendTrap_Type())
rbnDhcpIntfThresholdFallingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdFallingSendTrap.setStatus(_B)
_RbnDhcpIntfThresholdFallingLogMessage_Type=TruthValue
_RbnDhcpIntfThresholdFallingLogMessage_Object=MibTableColumn
rbnDhcpIntfThresholdFallingLogMessage=_RbnDhcpIntfThresholdFallingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,1,1,8),_RbnDhcpIntfThresholdFallingLogMessage_Type())
rbnDhcpIntfThresholdFallingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdFallingLogMessage.setStatus(_B)
class _RbnDhcpIntfThresholdRisingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpIntfThresholdRisingThreshold_Type.__name__=_D
_RbnDhcpIntfThresholdRisingThreshold_Object=MibTableColumn
rbnDhcpIntfThresholdRisingThreshold=_RbnDhcpIntfThresholdRisingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,1,1,9),_RbnDhcpIntfThresholdRisingThreshold_Type())
rbnDhcpIntfThresholdRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdRisingThreshold.setStatus(_B)
_RbnDhcpIntfThresholdRisingSendTrap_Type=TruthValue
_RbnDhcpIntfThresholdRisingSendTrap_Object=MibTableColumn
rbnDhcpIntfThresholdRisingSendTrap=_RbnDhcpIntfThresholdRisingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,1,1,10),_RbnDhcpIntfThresholdRisingSendTrap_Type())
rbnDhcpIntfThresholdRisingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdRisingSendTrap.setStatus(_B)
_RbnDhcpIntfThresholdRisingLogMessage_Type=TruthValue
_RbnDhcpIntfThresholdRisingLogMessage_Object=MibTableColumn
rbnDhcpIntfThresholdRisingLogMessage=_RbnDhcpIntfThresholdRisingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,1,1,11),_RbnDhcpIntfThresholdRisingLogMessage_Type())
rbnDhcpIntfThresholdRisingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpIntfThresholdRisingLogMessage.setStatus(_B)
_RbnDhcpCtxThreshold_ObjectIdentity=ObjectIdentity
rbnDhcpCtxThreshold=_RbnDhcpCtxThreshold_ObjectIdentity((1,3,6,1,4,1,2352,2,30,1,2))
class _RbnDhcpCtxThresholdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnDhcpCtxThresholdName_Type.__name__=_E
_RbnDhcpCtxThresholdName_Object=MibScalar
rbnDhcpCtxThresholdName=_RbnDhcpCtxThresholdName_Object((1,3,6,1,4,1,2352,2,30,1,2,1),_RbnDhcpCtxThresholdName_Type())
rbnDhcpCtxThresholdName.setMaxAccess(_S)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdName.setStatus(_B)
_RbnDhcpCtxThresholdSize_Type=Unsigned32
_RbnDhcpCtxThresholdSize_Object=MibScalar
rbnDhcpCtxThresholdSize=_RbnDhcpCtxThresholdSize_Object((1,3,6,1,4,1,2352,2,30,1,2,2),_RbnDhcpCtxThresholdSize_Type())
rbnDhcpCtxThresholdSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdSize.setStatus(_B)
_RbnDhcpCtxThresholdAvailable_Type=Unsigned32
_RbnDhcpCtxThresholdAvailable_Object=MibScalar
rbnDhcpCtxThresholdAvailable=_RbnDhcpCtxThresholdAvailable_Object((1,3,6,1,4,1,2352,2,30,1,2,3),_RbnDhcpCtxThresholdAvailable_Type())
rbnDhcpCtxThresholdAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdAvailable.setStatus(_B)
_RbnDhcpCtxThresholdInuse_Type=Unsigned32
_RbnDhcpCtxThresholdInuse_Object=MibScalar
rbnDhcpCtxThresholdInuse=_RbnDhcpCtxThresholdInuse_Object((1,3,6,1,4,1,2352,2,30,1,2,4),_RbnDhcpCtxThresholdInuse_Type())
rbnDhcpCtxThresholdInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdInuse.setStatus(_B)
class _RbnDhcpCtxThresholdFallingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpCtxThresholdFallingThreshold_Type.__name__=_D
_RbnDhcpCtxThresholdFallingThreshold_Object=MibScalar
rbnDhcpCtxThresholdFallingThreshold=_RbnDhcpCtxThresholdFallingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,2,5),_RbnDhcpCtxThresholdFallingThreshold_Type())
rbnDhcpCtxThresholdFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdFallingThreshold.setStatus(_B)
_RbnDhcpCtxThresholdFallingSendTrap_Type=TruthValue
_RbnDhcpCtxThresholdFallingSendTrap_Object=MibScalar
rbnDhcpCtxThresholdFallingSendTrap=_RbnDhcpCtxThresholdFallingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,2,6),_RbnDhcpCtxThresholdFallingSendTrap_Type())
rbnDhcpCtxThresholdFallingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdFallingSendTrap.setStatus(_B)
_RbnDhcpCtxThresholdFallingLogMessage_Type=TruthValue
_RbnDhcpCtxThresholdFallingLogMessage_Object=MibScalar
rbnDhcpCtxThresholdFallingLogMessage=_RbnDhcpCtxThresholdFallingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,2,7),_RbnDhcpCtxThresholdFallingLogMessage_Type())
rbnDhcpCtxThresholdFallingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdFallingLogMessage.setStatus(_B)
class _RbnDhcpCtxThresholdRisingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpCtxThresholdRisingThreshold_Type.__name__=_D
_RbnDhcpCtxThresholdRisingThreshold_Object=MibScalar
rbnDhcpCtxThresholdRisingThreshold=_RbnDhcpCtxThresholdRisingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,2,8),_RbnDhcpCtxThresholdRisingThreshold_Type())
rbnDhcpCtxThresholdRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdRisingThreshold.setStatus(_B)
_RbnDhcpCtxThresholdRisingSendTrap_Type=TruthValue
_RbnDhcpCtxThresholdRisingSendTrap_Object=MibScalar
rbnDhcpCtxThresholdRisingSendTrap=_RbnDhcpCtxThresholdRisingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,2,9),_RbnDhcpCtxThresholdRisingSendTrap_Type())
rbnDhcpCtxThresholdRisingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdRisingSendTrap.setStatus(_B)
_RbnDhcpCtxThresholdRisingLogMessage_Type=TruthValue
_RbnDhcpCtxThresholdRisingLogMessage_Object=MibScalar
rbnDhcpCtxThresholdRisingLogMessage=_RbnDhcpCtxThresholdRisingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,2,10),_RbnDhcpCtxThresholdRisingLogMessage_Type())
rbnDhcpCtxThresholdRisingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpCtxThresholdRisingLogMessage.setStatus(_B)
_RbnDhcpRangeThresholdTable_Object=MibTable
rbnDhcpRangeThresholdTable=_RbnDhcpRangeThresholdTable_Object((1,3,6,1,4,1,2352,2,30,1,3))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdTable.setStatus(_B)
_RbnDhcpRangeThresholdEntry_Object=MibTableRow
rbnDhcpRangeThresholdEntry=_RbnDhcpRangeThresholdEntry_Object((1,3,6,1,4,1,2352,2,30,1,3,1))
rbnDhcpRangeThresholdEntry.setIndexNames((0,_A,_v),(0,_A,_w))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdEntry.setStatus(_B)
_RbnDhcpRangeThresholdInterfaceIdx_Type=Unsigned32
_RbnDhcpRangeThresholdInterfaceIdx_Object=MibTableColumn
rbnDhcpRangeThresholdInterfaceIdx=_RbnDhcpRangeThresholdInterfaceIdx_Object((1,3,6,1,4,1,2352,2,30,1,3,1,1),_RbnDhcpRangeThresholdInterfaceIdx_Type())
rbnDhcpRangeThresholdInterfaceIdx.setMaxAccess(_R)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdInterfaceIdx.setStatus(_B)
_RbnDhcpRangeThresholdAddr_Type=IpAddress
_RbnDhcpRangeThresholdAddr_Object=MibTableColumn
rbnDhcpRangeThresholdAddr=_RbnDhcpRangeThresholdAddr_Object((1,3,6,1,4,1,2352,2,30,1,3,1,2),_RbnDhcpRangeThresholdAddr_Type())
rbnDhcpRangeThresholdAddr.setMaxAccess(_R)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdAddr.setStatus(_B)
_RbnDhcpRangeThresholdEndAddr_Type=IpAddress
_RbnDhcpRangeThresholdEndAddr_Object=MibTableColumn
rbnDhcpRangeThresholdEndAddr=_RbnDhcpRangeThresholdEndAddr_Object((1,3,6,1,4,1,2352,2,30,1,3,1,3),_RbnDhcpRangeThresholdEndAddr_Type())
rbnDhcpRangeThresholdEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdEndAddr.setStatus(_B)
class _RbnDhcpRangeThresholdContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnDhcpRangeThresholdContextName_Type.__name__=_E
_RbnDhcpRangeThresholdContextName_Object=MibTableColumn
rbnDhcpRangeThresholdContextName=_RbnDhcpRangeThresholdContextName_Object((1,3,6,1,4,1,2352,2,30,1,3,1,4),_RbnDhcpRangeThresholdContextName_Type())
rbnDhcpRangeThresholdContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdContextName.setStatus(_B)
class _RbnDhcpRangeThresholdInterfaceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_RbnDhcpRangeThresholdInterfaceName_Type.__name__=_E
_RbnDhcpRangeThresholdInterfaceName_Object=MibTableColumn
rbnDhcpRangeThresholdInterfaceName=_RbnDhcpRangeThresholdInterfaceName_Object((1,3,6,1,4,1,2352,2,30,1,3,1,5),_RbnDhcpRangeThresholdInterfaceName_Type())
rbnDhcpRangeThresholdInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdInterfaceName.setStatus(_B)
_RbnDhcpRangeThresholdSize_Type=Unsigned32
_RbnDhcpRangeThresholdSize_Object=MibTableColumn
rbnDhcpRangeThresholdSize=_RbnDhcpRangeThresholdSize_Object((1,3,6,1,4,1,2352,2,30,1,3,1,6),_RbnDhcpRangeThresholdSize_Type())
rbnDhcpRangeThresholdSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdSize.setStatus(_B)
_RbnDhcpRangeThresholdAvailable_Type=Unsigned32
_RbnDhcpRangeThresholdAvailable_Object=MibTableColumn
rbnDhcpRangeThresholdAvailable=_RbnDhcpRangeThresholdAvailable_Object((1,3,6,1,4,1,2352,2,30,1,3,1,7),_RbnDhcpRangeThresholdAvailable_Type())
rbnDhcpRangeThresholdAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdAvailable.setStatus(_B)
_RbnDhcpRangeThresholdInuse_Type=Unsigned32
_RbnDhcpRangeThresholdInuse_Object=MibTableColumn
rbnDhcpRangeThresholdInuse=_RbnDhcpRangeThresholdInuse_Object((1,3,6,1,4,1,2352,2,30,1,3,1,8),_RbnDhcpRangeThresholdInuse_Type())
rbnDhcpRangeThresholdInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdInuse.setStatus(_B)
class _RbnDhcpRangeThresholdFallingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpRangeThresholdFallingThreshold_Type.__name__=_D
_RbnDhcpRangeThresholdFallingThreshold_Object=MibTableColumn
rbnDhcpRangeThresholdFallingThreshold=_RbnDhcpRangeThresholdFallingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,3,1,9),_RbnDhcpRangeThresholdFallingThreshold_Type())
rbnDhcpRangeThresholdFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdFallingThreshold.setStatus(_B)
_RbnDhcpRangeThresholdFallingSendTrap_Type=TruthValue
_RbnDhcpRangeThresholdFallingSendTrap_Object=MibTableColumn
rbnDhcpRangeThresholdFallingSendTrap=_RbnDhcpRangeThresholdFallingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,3,1,10),_RbnDhcpRangeThresholdFallingSendTrap_Type())
rbnDhcpRangeThresholdFallingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdFallingSendTrap.setStatus(_B)
_RbnDhcpRangeThresholdFallingLogMessage_Type=TruthValue
_RbnDhcpRangeThresholdFallingLogMessage_Object=MibTableColumn
rbnDhcpRangeThresholdFallingLogMessage=_RbnDhcpRangeThresholdFallingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,3,1,11),_RbnDhcpRangeThresholdFallingLogMessage_Type())
rbnDhcpRangeThresholdFallingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdFallingLogMessage.setStatus(_B)
class _RbnDhcpRangeThresholdRisingThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,196608))
_RbnDhcpRangeThresholdRisingThreshold_Type.__name__=_D
_RbnDhcpRangeThresholdRisingThreshold_Object=MibTableColumn
rbnDhcpRangeThresholdRisingThreshold=_RbnDhcpRangeThresholdRisingThreshold_Object((1,3,6,1,4,1,2352,2,30,1,3,1,12),_RbnDhcpRangeThresholdRisingThreshold_Type())
rbnDhcpRangeThresholdRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdRisingThreshold.setStatus(_B)
_RbnDhcpRangeThresholdRisingSendTrap_Type=TruthValue
_RbnDhcpRangeThresholdRisingSendTrap_Object=MibTableColumn
rbnDhcpRangeThresholdRisingSendTrap=_RbnDhcpRangeThresholdRisingSendTrap_Object((1,3,6,1,4,1,2352,2,30,1,3,1,13),_RbnDhcpRangeThresholdRisingSendTrap_Type())
rbnDhcpRangeThresholdRisingSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdRisingSendTrap.setStatus(_B)
_RbnDhcpRangeThresholdRisingLogMessage_Type=TruthValue
_RbnDhcpRangeThresholdRisingLogMessage_Object=MibTableColumn
rbnDhcpRangeThresholdRisingLogMessage=_RbnDhcpRangeThresholdRisingLogMessage_Object((1,3,6,1,4,1,2352,2,30,1,3,1,14),_RbnDhcpRangeThresholdRisingLogMessage_Type())
rbnDhcpRangeThresholdRisingLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDhcpRangeThresholdRisingLogMessage.setStatus(_B)
_RbnDhcpLeaseFileStorageSlot_Type=RbnSlot
_RbnDhcpLeaseFileStorageSlot_Object=MibScalar
rbnDhcpLeaseFileStorageSlot=_RbnDhcpLeaseFileStorageSlot_Object((1,3,6,1,4,1,2352,2,30,1,4),_RbnDhcpLeaseFileStorageSlot_Type())
rbnDhcpLeaseFileStorageSlot.setMaxAccess(_S)
if mibBuilder.loadTexts:rbnDhcpLeaseFileStorageSlot.setStatus(_B)
class _RbnDhcpLeaseFileErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('storageDeviceDegraded',1),('storageDeviceFailed',2)))
_RbnDhcpLeaseFileErrorType_Type.__name__=_t
_RbnDhcpLeaseFileErrorType_Object=MibScalar
rbnDhcpLeaseFileErrorType=_RbnDhcpLeaseFileErrorType_Object((1,3,6,1,4,1,2352,2,30,1,5),_RbnDhcpLeaseFileErrorType_Type())
rbnDhcpLeaseFileErrorType.setMaxAccess(_S)
if mibBuilder.loadTexts:rbnDhcpLeaseFileErrorType.setStatus(_B)
_RbnDhcpMIBConformance_ObjectIdentity=ObjectIdentity
rbnDhcpMIBConformance=_RbnDhcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,30,2))
_RbnDhcpCompliances_ObjectIdentity=ObjectIdentity
rbnDhcpCompliances=_RbnDhcpCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,30,2,1))
_RbnDhcpGroups_ObjectIdentity=ObjectIdentity
rbnDhcpGroups=_RbnDhcpGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,30,2,2))
rbnDhcpThresholdGroup=ObjectGroup((1,3,6,1,4,1,2352,2,30,2,2,1))
rbnDhcpThresholdGroup.setObjects(*((_A,_I),(_A,_T),(_A,_U),(_A,_F),(_A,_J),(_A,_V),(_A,_W),(_A,_K),(_A,_X),(_A,_Y),(_A,_G),(_A,_Z),(_A,_H),(_A,_a),(_A,_L),(_A,_b),(_A,_c),(_A,_M),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:rbnDhcpThresholdGroup.setStatus(_B)
rbnDhcpIntfThresholdGroup=ObjectGroup((1,3,6,1,4,1,2352,2,30,2,2,3))
rbnDhcpIntfThresholdGroup.setObjects(*((_A,_T),(_A,_U),(_A,_F),(_A,_J),(_A,_V),(_A,_W),(_A,_K),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdGroup.setStatus(_B)
rbnDhcpCtxThresholdGroup=ObjectGroup((1,3,6,1,4,1,2352,2,30,2,2,4))
rbnDhcpCtxThresholdGroup.setObjects(*((_A,_G),(_A,_Z),(_A,_H),(_A,_a),(_A,_L),(_A,_b),(_A,_c),(_A,_M),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:rbnDhcpCtxThresholdGroup.setStatus(_B)
rbnDhcpRangeThresholdGroup=ObjectGroup((1,3,6,1,4,1,2352,2,30,2,2,5))
rbnDhcpRangeThresholdGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_x),(_A,_y),(_A,_Q),(_A,_f),(_A,_z),(_A,_A0),(_A,_g),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdGroup.setStatus(_B)
rbnDhcpLeaseFileFailureTrapGroup=ObjectGroup((1,3,6,1,4,1,2352,2,30,2,2,9))
rbnDhcpLeaseFileFailureTrapGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:rbnDhcpLeaseFileFailureTrapGroup.setStatus(_B)
rbnDhcpIntfThresholdFallingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,1))
rbnDhcpIntfThresholdFallingThresholdMet.setObjects(*((_A,_I),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdFallingThresholdMet.setStatus(_B)
rbnDhcpIntfThresholdRisingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,2))
rbnDhcpIntfThresholdRisingThresholdMet.setObjects(*((_A,_I),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdRisingThresholdMet.setStatus(_B)
rbnDhcpCtxThresholdFallingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,3))
rbnDhcpCtxThresholdFallingThresholdMet.setObjects(*((_A,_G),(_A,_H),(_A,_L)))
if mibBuilder.loadTexts:rbnDhcpCtxThresholdFallingThresholdMet.setStatus(_B)
rbnDhcpCtxThresholdRisingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,4))
rbnDhcpCtxThresholdRisingThresholdMet.setObjects(*((_A,_G),(_A,_H),(_A,_M)))
if mibBuilder.loadTexts:rbnDhcpCtxThresholdRisingThresholdMet.setStatus(_B)
rbnDhcpRangeThresholdFallingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,5))
rbnDhcpRangeThresholdFallingThresholdMet.setObjects(*((_A,_O),(_A,_P),(_A,_N),(_A,_Q),(_A,_f)))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdFallingThresholdMet.setStatus(_B)
rbnDhcpRangeThresholdRisingThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,30,0,6))
rbnDhcpRangeThresholdRisingThresholdMet.setObjects(*((_A,_O),(_A,_P),(_A,_N),(_A,_Q),(_A,_g)))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdRisingThresholdMet.setStatus(_B)
rbnDhcpLeaseFileFailure=NotificationType((1,3,6,1,4,1,2352,2,30,0,7))
rbnDhcpLeaseFileFailure.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:rbnDhcpLeaseFileFailure.setStatus(_B)
rbnDhcpThresholdNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,30,2,2,2))
rbnDhcpThresholdNotifyGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:rbnDhcpThresholdNotifyGroup.setStatus(_B)
rbnDhcpIntfThresholdNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,30,2,2,6))
rbnDhcpIntfThresholdNotifyGroup.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:rbnDhcpIntfThresholdNotifyGroup.setStatus(_B)
rbnDhcpCtxThresholdNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,30,2,2,7))
rbnDhcpCtxThresholdNotifyGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:rbnDhcpCtxThresholdNotifyGroup.setStatus(_B)
rbnDhcpRangeThresholdNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,30,2,2,8))
rbnDhcpRangeThresholdNotifyGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:rbnDhcpRangeThresholdNotifyGroup.setStatus(_B)
rbnDhcpLeaseFileFailureNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,30,2,2,10))
rbnDhcpLeaseFileFailureNotifyGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:rbnDhcpLeaseFileFailureNotifyGroup.setStatus(_B)
rbnDhcpThresholdCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,30,2,1,1))
rbnDhcpThresholdCompliance.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:rbnDhcpThresholdCompliance.setStatus(_B)
rbnDhcpThresholdCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,30,2,1,2))
rbnDhcpThresholdCompliance2.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:rbnDhcpThresholdCompliance2.setStatus('deprecated')
rbnDhcpThresholdCompliance3=ModuleCompliance((1,3,6,1,4,1,2352,2,30,2,1,3))
rbnDhcpThresholdCompliance3.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:rbnDhcpThresholdCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnDhcpMib':rbnDhcpMib,'rbnDhcpMIBNotifications':rbnDhcpMIBNotifications,_j:rbnDhcpIntfThresholdFallingThresholdMet,_k:rbnDhcpIntfThresholdRisingThresholdMet,_l:rbnDhcpCtxThresholdFallingThresholdMet,_m:rbnDhcpCtxThresholdRisingThresholdMet,_A3:rbnDhcpRangeThresholdFallingThresholdMet,_A4:rbnDhcpRangeThresholdRisingThresholdMet,_A5:rbnDhcpLeaseFileFailure,'rbnDhcpMIBObjects':rbnDhcpMIBObjects,'rbnDhcpIntfThresholdTable':rbnDhcpIntfThresholdTable,'rbnDhcpIntfThresholdEntry':rbnDhcpIntfThresholdEntry,_u:rbnDhcpIntfThresholdName,_I:rbnDhcpIntfThresholdContextName,_T:rbnDhcpIntfThresholdSize,_F:rbnDhcpIntfThresholdAvailable,_U:rbnDhcpIntfThresholdInuse,_J:rbnDhcpIntfThresholdFallingThreshold,_V:rbnDhcpIntfThresholdFallingSendTrap,_W:rbnDhcpIntfThresholdFallingLogMessage,_K:rbnDhcpIntfThresholdRisingThreshold,_X:rbnDhcpIntfThresholdRisingSendTrap,_Y:rbnDhcpIntfThresholdRisingLogMessage,'rbnDhcpCtxThreshold':rbnDhcpCtxThreshold,_G:rbnDhcpCtxThresholdName,_Z:rbnDhcpCtxThresholdSize,_H:rbnDhcpCtxThresholdAvailable,_a:rbnDhcpCtxThresholdInuse,_L:rbnDhcpCtxThresholdFallingThreshold,_b:rbnDhcpCtxThresholdFallingSendTrap,_c:rbnDhcpCtxThresholdFallingLogMessage,_M:rbnDhcpCtxThresholdRisingThreshold,_d:rbnDhcpCtxThresholdRisingSendTrap,_e:rbnDhcpCtxThresholdRisingLogMessage,'rbnDhcpRangeThresholdTable':rbnDhcpRangeThresholdTable,'rbnDhcpRangeThresholdEntry':rbnDhcpRangeThresholdEntry,_v:rbnDhcpRangeThresholdInterfaceIdx,_w:rbnDhcpRangeThresholdAddr,_N:rbnDhcpRangeThresholdEndAddr,_O:rbnDhcpRangeThresholdContextName,_P:rbnDhcpRangeThresholdInterfaceName,_x:rbnDhcpRangeThresholdSize,_Q:rbnDhcpRangeThresholdAvailable,_y:rbnDhcpRangeThresholdInuse,_f:rbnDhcpRangeThresholdFallingThreshold,_z:rbnDhcpRangeThresholdFallingSendTrap,_A0:rbnDhcpRangeThresholdFallingLogMessage,_g:rbnDhcpRangeThresholdRisingThreshold,_A1:rbnDhcpRangeThresholdRisingSendTrap,_A2:rbnDhcpRangeThresholdRisingLogMessage,_h:rbnDhcpLeaseFileStorageSlot,_i:rbnDhcpLeaseFileErrorType,'rbnDhcpMIBConformance':rbnDhcpMIBConformance,'rbnDhcpCompliances':rbnDhcpCompliances,'rbnDhcpThresholdCompliance':rbnDhcpThresholdCompliance,'rbnDhcpThresholdCompliance2':rbnDhcpThresholdCompliance2,'rbnDhcpThresholdCompliance3':rbnDhcpThresholdCompliance3,'rbnDhcpGroups':rbnDhcpGroups,_A6:rbnDhcpThresholdGroup,_A7:rbnDhcpThresholdNotifyGroup,_n:rbnDhcpIntfThresholdGroup,_o:rbnDhcpCtxThresholdGroup,_p:rbnDhcpRangeThresholdGroup,_q:rbnDhcpIntfThresholdNotifyGroup,_r:rbnDhcpCtxThresholdNotifyGroup,_s:rbnDhcpRangeThresholdNotifyGroup,_A8:rbnDhcpLeaseFileFailureTrapGroup,_A9:rbnDhcpLeaseFileFailureNotifyGroup})