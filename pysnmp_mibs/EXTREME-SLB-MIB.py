_H='extremeSlbRealAppPort'
_G='extremeSlbRealAppIpAddress'
_F='read-write'
_E='extremeSlbRealServerIpAddress'
_D='Integer32'
_C='not-accessible'
_B='EXTREME-SLB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
extremeSlb=ModuleIdentity((1,3,6,1,4,1,1916,1,14))
_ExtremeSlbRealServerTable_Object=MibTable
extremeSlbRealServerTable=_ExtremeSlbRealServerTable_Object((1,3,6,1,4,1,1916,1,14,1))
if mibBuilder.loadTexts:extremeSlbRealServerTable.setStatus(_A)
_ExtremeSlbRealServerEntry_Object=MibTableRow
extremeSlbRealServerEntry=_ExtremeSlbRealServerEntry_Object((1,3,6,1,4,1,1916,1,14,1,1))
extremeSlbRealServerEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:extremeSlbRealServerEntry.setStatus(_A)
_ExtremeSlbRealServerIpAddress_Type=IpAddress
_ExtremeSlbRealServerIpAddress_Object=MibTableColumn
extremeSlbRealServerIpAddress=_ExtremeSlbRealServerIpAddress_Object((1,3,6,1,4,1,1916,1,14,1,1,1),_ExtremeSlbRealServerIpAddress_Type())
extremeSlbRealServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeSlbRealServerIpAddress.setStatus(_A)
_ExtremeSlbRealServerUp_Type=TruthValue
_ExtremeSlbRealServerUp_Object=MibTableColumn
extremeSlbRealServerUp=_ExtremeSlbRealServerUp_Object((1,3,6,1,4,1,1916,1,14,1,1,2),_ExtremeSlbRealServerUp_Type())
extremeSlbRealServerUp.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeSlbRealServerUp.setStatus(_A)
_ExtremeSlbRealAppTable_Object=MibTable
extremeSlbRealAppTable=_ExtremeSlbRealAppTable_Object((1,3,6,1,4,1,1916,1,14,2))
if mibBuilder.loadTexts:extremeSlbRealAppTable.setStatus(_A)
_ExtremeSlbRealAppEntry_Object=MibTableRow
extremeSlbRealAppEntry=_ExtremeSlbRealAppEntry_Object((1,3,6,1,4,1,1916,1,14,2,1))
extremeSlbRealAppEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:extremeSlbRealAppEntry.setStatus(_A)
_ExtremeSlbRealAppIpAddress_Type=IpAddress
_ExtremeSlbRealAppIpAddress_Object=MibTableColumn
extremeSlbRealAppIpAddress=_ExtremeSlbRealAppIpAddress_Object((1,3,6,1,4,1,1916,1,14,2,1,1),_ExtremeSlbRealAppIpAddress_Type())
extremeSlbRealAppIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeSlbRealAppIpAddress.setStatus(_A)
class _ExtremeSlbRealAppPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeSlbRealAppPort_Type.__name__=_D
_ExtremeSlbRealAppPort_Object=MibTableColumn
extremeSlbRealAppPort=_ExtremeSlbRealAppPort_Object((1,3,6,1,4,1,1916,1,14,2,1,2),_ExtremeSlbRealAppPort_Type())
extremeSlbRealAppPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeSlbRealAppPort.setStatus(_A)
_ExtremeSlbRealAppUp_Type=TruthValue
_ExtremeSlbRealAppUp_Object=MibTableColumn
extremeSlbRealAppUp=_ExtremeSlbRealAppUp_Object((1,3,6,1,4,1,1916,1,14,2,1,3),_ExtremeSlbRealAppUp_Type())
extremeSlbRealAppUp.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeSlbRealAppUp.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeSlb':extremeSlb,'extremeSlbRealServerTable':extremeSlbRealServerTable,'extremeSlbRealServerEntry':extremeSlbRealServerEntry,_E:extremeSlbRealServerIpAddress,'extremeSlbRealServerUp':extremeSlbRealServerUp,'extremeSlbRealAppTable':extremeSlbRealAppTable,'extremeSlbRealAppEntry':extremeSlbRealAppEntry,_G:extremeSlbRealAppIpAddress,_H:extremeSlbRealAppPort,'extremeSlbRealAppUp':extremeSlbRealAppUp})