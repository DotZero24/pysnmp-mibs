_L='zyAntiArpscanHostVid'
_K='zyAntiArpscanHostMacAddress'
_J='zyAntiArpscanTrustHostMask'
_I='zyAntiArpscanTrustHostIpAddress'
_H='dot1dBasePort'
_G='BRIDGE-MIB'
_F='not-accessible'
_E='read-only'
_D='ZYXEL-ANTI-ARPSCAN-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_G,_H)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelAntiArpscan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,106))
_ZyxelAntiArpscanSetup_ObjectIdentity=ObjectIdentity
zyxelAntiArpscanSetup=_ZyxelAntiArpscanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,106,1))
_ZyAntiArpscanState_Type=EnabledStatus
_ZyAntiArpscanState_Object=MibScalar
zyAntiArpscanState=_ZyAntiArpscanState_Object((1,3,6,1,4,1,890,1,15,3,106,1,1),_ZyAntiArpscanState_Type())
zyAntiArpscanState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanState.setStatus(_A)
class _ZyAntiArpscanPortThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,255))
_ZyAntiArpscanPortThreshold_Type.__name__=_C
_ZyAntiArpscanPortThreshold_Object=MibScalar
zyAntiArpscanPortThreshold=_ZyAntiArpscanPortThreshold_Object((1,3,6,1,4,1,890,1,15,3,106,1,2),_ZyAntiArpscanPortThreshold_Type())
zyAntiArpscanPortThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanPortThreshold.setStatus(_A)
class _ZyAntiArpscanHostThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100))
_ZyAntiArpscanHostThreshold_Type.__name__=_C
_ZyAntiArpscanHostThreshold_Object=MibScalar
zyAntiArpscanHostThreshold=_ZyAntiArpscanHostThreshold_Object((1,3,6,1,4,1,890,1,15,3,106,1,3),_ZyAntiArpscanHostThreshold_Type())
zyAntiArpscanHostThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanHostThreshold.setStatus(_A)
_ZyxelAntiArpscanPortTable_Object=MibTable
zyxelAntiArpscanPortTable=_ZyxelAntiArpscanPortTable_Object((1,3,6,1,4,1,890,1,15,3,106,1,4))
if mibBuilder.loadTexts:zyxelAntiArpscanPortTable.setStatus(_A)
_ZyxelAntiArpscanPortEntry_Object=MibTableRow
zyxelAntiArpscanPortEntry=_ZyxelAntiArpscanPortEntry_Object((1,3,6,1,4,1,890,1,15,3,106,1,4,1))
zyxelAntiArpscanPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelAntiArpscanPortEntry.setStatus(_A)
class _ZyAntiArpscanPortTrustState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('untrusted',2)))
_ZyAntiArpscanPortTrustState_Type.__name__=_C
_ZyAntiArpscanPortTrustState_Object=MibTableColumn
zyAntiArpscanPortTrustState=_ZyAntiArpscanPortTrustState_Object((1,3,6,1,4,1,890,1,15,3,106,1,4,1,1),_ZyAntiArpscanPortTrustState_Type())
zyAntiArpscanPortTrustState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanPortTrustState.setStatus(_A)
_ZyAntiArpscanMaxNumberOfTrustHosts_Type=Integer32
_ZyAntiArpscanMaxNumberOfTrustHosts_Object=MibScalar
zyAntiArpscanMaxNumberOfTrustHosts=_ZyAntiArpscanMaxNumberOfTrustHosts_Object((1,3,6,1,4,1,890,1,15,3,106,1,5),_ZyAntiArpscanMaxNumberOfTrustHosts_Type())
zyAntiArpscanMaxNumberOfTrustHosts.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAntiArpscanMaxNumberOfTrustHosts.setStatus(_A)
_ZyxelAntiArpscanTrustHostTable_Object=MibTable
zyxelAntiArpscanTrustHostTable=_ZyxelAntiArpscanTrustHostTable_Object((1,3,6,1,4,1,890,1,15,3,106,1,6))
if mibBuilder.loadTexts:zyxelAntiArpscanTrustHostTable.setStatus(_A)
_ZyxelAntiArpscanTrustHostEntry_Object=MibTableRow
zyxelAntiArpscanTrustHostEntry=_ZyxelAntiArpscanTrustHostEntry_Object((1,3,6,1,4,1,890,1,15,3,106,1,6,1))
zyxelAntiArpscanTrustHostEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:zyxelAntiArpscanTrustHostEntry.setStatus(_A)
_ZyAntiArpscanTrustHostIpAddress_Type=IpAddress
_ZyAntiArpscanTrustHostIpAddress_Object=MibTableColumn
zyAntiArpscanTrustHostIpAddress=_ZyAntiArpscanTrustHostIpAddress_Object((1,3,6,1,4,1,890,1,15,3,106,1,6,1,1),_ZyAntiArpscanTrustHostIpAddress_Type())
zyAntiArpscanTrustHostIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zyAntiArpscanTrustHostIpAddress.setStatus(_A)
_ZyAntiArpscanTrustHostMask_Type=IpAddress
_ZyAntiArpscanTrustHostMask_Object=MibTableColumn
zyAntiArpscanTrustHostMask=_ZyAntiArpscanTrustHostMask_Object((1,3,6,1,4,1,890,1,15,3,106,1,6,1,2),_ZyAntiArpscanTrustHostMask_Type())
zyAntiArpscanTrustHostMask.setMaxAccess(_F)
if mibBuilder.loadTexts:zyAntiArpscanTrustHostMask.setStatus(_A)
_ZyAntiArpscanTrustHostName_Type=DisplayString
_ZyAntiArpscanTrustHostName_Object=MibTableColumn
zyAntiArpscanTrustHostName=_ZyAntiArpscanTrustHostName_Object((1,3,6,1,4,1,890,1,15,3,106,1,6,1,3),_ZyAntiArpscanTrustHostName_Type())
zyAntiArpscanTrustHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanTrustHostName.setStatus(_A)
_ZyAntiArpscanTrustHostRowStatus_Type=RowStatus
_ZyAntiArpscanTrustHostRowStatus_Object=MibTableColumn
zyAntiArpscanTrustHostRowStatus=_ZyAntiArpscanTrustHostRowStatus_Object((1,3,6,1,4,1,890,1,15,3,106,1,6,1,4),_ZyAntiArpscanTrustHostRowStatus_Type())
zyAntiArpscanTrustHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanTrustHostRowStatus.setStatus(_A)
_ZyxelAntiArpscanStatus_ObjectIdentity=ObjectIdentity
zyxelAntiArpscanStatus=_ZyxelAntiArpscanStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,106,2))
_ZyAntiArpscanHostClear_Type=Integer32
_ZyAntiArpscanHostClear_Object=MibScalar
zyAntiArpscanHostClear=_ZyAntiArpscanHostClear_Object((1,3,6,1,4,1,890,1,15,3,106,2,1),_ZyAntiArpscanHostClear_Type())
zyAntiArpscanHostClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAntiArpscanHostClear.setStatus(_A)
_ZyxelAntiArpscanHostTable_Object=MibTable
zyxelAntiArpscanHostTable=_ZyxelAntiArpscanHostTable_Object((1,3,6,1,4,1,890,1,15,3,106,2,2))
if mibBuilder.loadTexts:zyxelAntiArpscanHostTable.setStatus(_A)
_ZyxelAntiArpscanHostEntry_Object=MibTableRow
zyxelAntiArpscanHostEntry=_ZyxelAntiArpscanHostEntry_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1))
zyxelAntiArpscanHostEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:zyxelAntiArpscanHostEntry.setStatus(_A)
_ZyAntiArpscanHostMacAddress_Type=MacAddress
_ZyAntiArpscanHostMacAddress_Object=MibTableColumn
zyAntiArpscanHostMacAddress=_ZyAntiArpscanHostMacAddress_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1,1),_ZyAntiArpscanHostMacAddress_Type())
zyAntiArpscanHostMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zyAntiArpscanHostMacAddress.setStatus(_A)
class _ZyAntiArpscanHostVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyAntiArpscanHostVid_Type.__name__=_C
_ZyAntiArpscanHostVid_Object=MibTableColumn
zyAntiArpscanHostVid=_ZyAntiArpscanHostVid_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1,2),_ZyAntiArpscanHostVid_Type())
zyAntiArpscanHostVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zyAntiArpscanHostVid.setStatus(_A)
_ZyAntiArpscanHostPort_Type=Integer32
_ZyAntiArpscanHostPort_Object=MibTableColumn
zyAntiArpscanHostPort=_ZyAntiArpscanHostPort_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1,3),_ZyAntiArpscanHostPort_Type())
zyAntiArpscanHostPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAntiArpscanHostPort.setStatus(_A)
_ZyAntiArpscanHostIpAddress_Type=IpAddress
_ZyAntiArpscanHostIpAddress_Object=MibTableColumn
zyAntiArpscanHostIpAddress=_ZyAntiArpscanHostIpAddress_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1,4),_ZyAntiArpscanHostIpAddress_Type())
zyAntiArpscanHostIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAntiArpscanHostIpAddress.setStatus(_A)
class _ZyAntiArpscanHostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('errDisable',2))
_ZyAntiArpscanHostStatus_Type.__name__=_C
_ZyAntiArpscanHostStatus_Object=MibTableColumn
zyAntiArpscanHostStatus=_ZyAntiArpscanHostStatus_Object((1,3,6,1,4,1,890,1,15,3,106,2,2,1,5),_ZyAntiArpscanHostStatus_Type())
zyAntiArpscanHostStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAntiArpscanHostStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelAntiArpscan':zyxelAntiArpscan,'zyxelAntiArpscanSetup':zyxelAntiArpscanSetup,'zyAntiArpscanState':zyAntiArpscanState,'zyAntiArpscanPortThreshold':zyAntiArpscanPortThreshold,'zyAntiArpscanHostThreshold':zyAntiArpscanHostThreshold,'zyxelAntiArpscanPortTable':zyxelAntiArpscanPortTable,'zyxelAntiArpscanPortEntry':zyxelAntiArpscanPortEntry,'zyAntiArpscanPortTrustState':zyAntiArpscanPortTrustState,'zyAntiArpscanMaxNumberOfTrustHosts':zyAntiArpscanMaxNumberOfTrustHosts,'zyxelAntiArpscanTrustHostTable':zyxelAntiArpscanTrustHostTable,'zyxelAntiArpscanTrustHostEntry':zyxelAntiArpscanTrustHostEntry,_I:zyAntiArpscanTrustHostIpAddress,_J:zyAntiArpscanTrustHostMask,'zyAntiArpscanTrustHostName':zyAntiArpscanTrustHostName,'zyAntiArpscanTrustHostRowStatus':zyAntiArpscanTrustHostRowStatus,'zyxelAntiArpscanStatus':zyxelAntiArpscanStatus,'zyAntiArpscanHostClear':zyAntiArpscanHostClear,'zyxelAntiArpscanHostTable':zyxelAntiArpscanHostTable,'zyxelAntiArpscanHostEntry':zyxelAntiArpscanHostEntry,_K:zyAntiArpscanHostMacAddress,_L:zyAntiArpscanHostVid,'zyAntiArpscanHostPort':zyAntiArpscanHostPort,'zyAntiArpscanHostIpAddress':zyAntiArpscanHostIpAddress,'zyAntiArpscanHostStatus':zyAntiArpscanHostStatus})